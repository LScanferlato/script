$Path = “E:\Polybox”
$Path2 = “E:\Modelli”
$Daysback = “-150”
$DaysbackPath2 = “-1”


$CurrentDate = Get-Date
$DatetoDelete = $CurrentDate.AddDays($Daysback)
$FilesToDelete = Get-ChildItem $Path -Recurse -File | Where-Object { $_.LastWriteTime -lt $DatetoDelete }
$FilesToDelete | out-file e:\Polybox\FilesDeleted.txt
$FilesToDelete | Remove-Item

$DatetoDelete = $CurrentDate.AddDays($DaysbackPath2)
$FilesToDelete = Get-ChildItem $Path2 -Recurse -File | Where-Object { $_.LastWriteTime -lt $DatetoDelete }
$FilesToDelete | Remove-Item

$Date = (Get-Date -format "yyyyMMdd")
Get-ChildItem -Recurse "E:\Polybox\" | Where { ! $_.PSIsContainer } |  Where {! $_.PSIsContainer } | Select FullName,LastWriteTime > E:\Polybox\Status\$Date.txt
