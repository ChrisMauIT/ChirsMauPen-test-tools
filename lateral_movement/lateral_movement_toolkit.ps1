<#
  Automates basic lateral movement using PsExec and WMI.
#>

$targets = Get-Content targets.txt
$creds = Get-Credential

foreach ($target in $targets) {
    Invoke-Command -ComputerName $target -ScriptBlock {
        whoami
        Get-LocalGroupMember Administrators
    } -Credential $creds
}
