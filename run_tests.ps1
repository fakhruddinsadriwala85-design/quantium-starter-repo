
& .\venv\Scripts\Activate.ps1


pytest test_app.py

if ($LASTEXITCODE -eq 0) {
    Write-Output "All tests passed!"
    exit 0
} else {
    Write-Output "Some tests failed!"
    exit 1
}
