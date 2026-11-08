# Optional Windows/Office validation; opens read-only without showing a window.
$ErrorActionPreference = 'Stop'
$deckPath = Join-Path $PSScriptRoot '../documentation/portfolio_presentation.pptx'
$deckPath = (Resolve-Path -LiteralPath $deckPath).Path
$outputPath = Join-Path (Split-Path $deckPath) 'portfolio_presentation_preview.pdf'
$previewFolder = Join-Path (Split-Path $deckPath) 'slide_previews'
New-Item -ItemType Directory -Path $previewFolder -Force | Out-Null
$powerPointApp = New-Object -ComObject PowerPoint.Application
try {
    $powerPointApp.DisplayAlerts = 1
    $openedDeck = $powerPointApp.Presentations.Open($deckPath, -1, 0, 0)
    try {
        $openedDeck.SaveAs($outputPath, 32)
        for ($index = 1; $index -le $openedDeck.Slides.Count; $index++) {
            $imagePath = Join-Path $previewFolder ('slide-{0:00}.png' -f $index)
            $openedDeck.Slides.Item($index).Export($imagePath, 'PNG', 1600, 900)
        }
        Write-Output ('PowerPoint opened and exported ' + $openedDeck.Slides.Count + ' slides.')
    } finally {
        $openedDeck.Close()
        [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($openedDeck)
    }
} finally {
    $powerPointApp.Quit()
    [void][System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPointApp)
}
