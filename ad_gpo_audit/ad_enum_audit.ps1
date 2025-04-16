<#
  Audits key AD and GPO settings for privilege escalation potential.
#>

# List Domain Admins
Get-ADGroupMember "Domain Admins" | Select Name, SamAccountName

# List GPOs with potentially dangerous permissions
Get-GPO -All | ForEach-Object {
    Get-GPPermission -Guid $_.Id -All | Where-Object {$_.Permission -like "*Write*"}
}
