function getIP{
    (Get-NetIPAddress).ipv4address | Select-String "192*"
}

$IP = getIP

Write-Host("This machine's IP is $IP")
