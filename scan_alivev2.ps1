#Fernando Javier Marin Salas
#1679139
$subred = (Get-Netroute -DestinationPrefix 0.0.0.0/0).NextHop
Write-Host "==Determinando tu gateway ..."
Write-Host "Tu gateway:" $subred

$rango = $subred.Substring(0,$subred.IndexOf(".")+1+$subred.Substring($subred.IndexOf(".")+1).IndexOf(".")+3)
Write-Host "== Determinando tu rango de subred ..."
echo $rango

$punto = $rango.EndsWith(".")
if ($punto -Like "False")
{
	$rango = $rango + "."
}

$rango_ip = @(1..254)

Write-Output ""
Write-Host "--Subred actual:"
Write-Host "Escaneando:" -NoNewLine; Write-Host $rango -NoNewLine; Write-Host "0/24" -ForegroundColor Red
Write-Output ""

foreach ($r in $rango_ip)
{
	$actual = $rango + $r
	$responde = Test-Connection $actual -Quiet -Count 1
	if ($responde -eq "True")
	{
		Write-Output ""
		Write-Host "Host responde:" -NoNewLine; Write-Host $actual -ForegroundColor Green
	}
}
