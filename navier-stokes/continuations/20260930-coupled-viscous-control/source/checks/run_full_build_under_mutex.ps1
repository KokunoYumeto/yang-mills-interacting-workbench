$ErrorActionPreference = 'Stop'

$mutexName = 'Global\InterlanguageTeXSlotV1'
$receiptPath = Join-Path $PSScriptRoot 'infinite_similarity_tex_slot_receipt.json'
$laneRoot = Split-Path -Parent $PSScriptRoot
$started = [DateTime]::UtcNow.ToString('o')
$slot = [System.Threading.Mutex]::new($false, $mutexName)
$held = $false
$abandoned = $false
$buildStarted = $false
$compilerAvailable = $false
$buildExit = $null
$outcome = 'error'
$exitCode = 1

try {
    try {
        $held = $slot.WaitOne(1000)
    }
    catch [System.Threading.AbandonedMutexException] {
        $held = $true
        $abandoned = $true
    }

    if (-not $held) {
        $outcome = 'occupied'
        $exitCode = 75
    }
    else {
        $compilerAvailable = $null -ne (Get-Command pdflatex -ErrorAction SilentlyContinue)
        if (-not $compilerAvailable) {
            $outcome = 'compiler_unavailable'
            $exitCode = 69
        }
        else {
            $buildStarted = $true
            & python (Join-Path $laneRoot 'build_and_verify.py')
            $buildExit = $LASTEXITCODE
            $exitCode = $buildExit
            if ($buildExit -eq 0) {
                $outcome = 'passed'
            }
            else {
                $outcome = 'build_failed'
            }
        }
    }
}
finally {
    if ($held) {
        $slot.ReleaseMutex()
    }
    $slot.Dispose()
    $attempt = [ordered]@{
        started_at = $started
        recorded_at = [DateTime]::UtcNow.ToString('o')
        outcome = $outcome
        exit_code = $exitCode
        slot_acquired = $held
        abandoned_mutex_recovered = $abandoned
        compiler_available = $compilerAvailable
        build_process_started = $buildStarted
        build_exit_code = $buildExit
        full_child_lifetime_protected = $held -and $buildStarted
        pdf_rebuilt = $outcome -eq 'passed'
    }
    $attempts = @()
    if (Test-Path -LiteralPath $receiptPath) {
        try {
            $prior = Get-Content -LiteralPath $receiptPath -Raw | ConvertFrom-Json
            if ($prior.schema -eq 'interlanguage-tex-slot-attempts-v2') {
                $attempts = @($prior.attempts)
            }
            elseif ($prior.schema -eq 'interlanguage-tex-slot-attempt-v1') {
                $attempts = @($prior)
            }
        }
        catch {
            $attempts = @()
        }
    }
    $attempts += $attempt
    $receipt = [ordered]@{
        schema = 'interlanguage-tex-slot-attempts-v2'
        mutex = $mutexName
        scope = 'cumulative coupled-viscous-control reader after fixed-diffusion similarity integration'
        attempt_count = $attempts.Count
        attempts = $attempts
        latest_outcome = $outcome
        pdf_rebuilt = $outcome -eq 'passed'
    }
    $receipt | ConvertTo-Json -Depth 4 | Set-Content -LiteralPath $receiptPath -Encoding utf8
}

exit $exitCode
