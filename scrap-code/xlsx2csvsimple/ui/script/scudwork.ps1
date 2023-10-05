$UserList=IMPORT-CSV "C:\SCUD 2023\scudADwork.csv"
 
FOREACH ($Person in $UserList) {
 
$Domain="@ULSPU.RU"
$FullName=$Person.cn
$Company=$Person.company
$Department=$Person.department
$Description=$Person.description
$givenName=$Person.givenName
$initials=$Person.initials
$I=$Person.City
$sAMAccountName=$Person.sAMAccountName
$sn=$Person.sn
$userPrincipalName=$Person.sAMAccountName+$Domain
$userPassword=$Person.userPassword
$expire=$null
 
NEW-ADUSER -PassThru -Path "OU=‘¿-23, OU=‘»ﬂ, OU=Students, DC=ULSPU,DC=RU" -Enabled $True -AccountExpirationDate $expire -ChangePasswordAtLogon $False -AccountPassword (ConvertTo-SecureString $userPassword -AsPlainText -Force) -CannotChangePassword $True -City $I -Company $Company -Department $Department -Description $Description -DisplayName $FullName -GivenName $givenName -Initials $initials -Name $FullName -SamAccountName $sAMAccountName -Surname $sn -Title $Description -UserPrincipalName $userPrincipalName
 
Set-ADAccountControl $sAMAccountName -PasswordNeverExpires $True
}

pause