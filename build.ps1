$requirementsPath = "requirements.txt"
$platform = "win_amd64"
$libPath = "release\lib"
$basePath = "."
$tmpPath = "release\tmp"
$apworldBuildPath = "release\tmp\bfbb"
$apworldOutPath = "release\bfbb.apworld"
$apworldOutZip = "release\tmp\bfbb.zip"

Remove-Item -Recurse -Force -Path "release\lib"

pip3.8 install --target $libPath --platform $platform --only-binary :all: --requirement $requirementsPath --upgrade
pip3.11 install --target $libPath --platform $platform --only-binary :all: --requirement $requirementsPath --upgrade
pip3.12 install --target $libPath --platform $platform --only-binary :all: --requirement $requirementsPath --upgrade

# Find all .dist-info folders in the lib directory
Get-ChildItem -Path $libPath -Recurse -Directory -Filter "*.dist-info" | ForEach-Object {
    $distInfoFolder = $_.FullName
    $packageName = $_.Name -replace '\.dist-info$', ''

    # Check for LICENSE or equivalent files in the .dist-info folder
    $licenseFile = Get-ChildItem -Path $distInfoFolder -Filter "LICENSE*" -ErrorAction SilentlyContinue
    if ($licenseFile) {
        # Rename and move the license file one layer up
        $newLicenseName = Join-Path $libPath "$packageName.LICENSE"
        Move-Item -Path $licenseFile.FullName -Destination $newLicenseName
    }

    # Delete the .dist-info folder
    Remove-Item -Recurse -Force -Path $distInfoFolder
}
# Remove __pycache__ folders if they exist
Get-ChildItem -Path $libPath -Recurse -Directory -Filter "__pycache__" | ForEach-Object {
    Remove-Item -Recurse -Force -Path $_.FullName
}

# build apworld
# copy base files needed
robocopy $basePath $apworldBuildPath /MIR /XD IP_src IndustrialPark-EditorFiles __pycache__ release .git /XF .gitignore .gitmodules *.ps1 TODO.md
# remove old apworld
Remove-Item -Force -Path $apworldOutZip
# zip it
#Compress-Archive -Path $apworldBuildPath -DestinationPath $apworldOutZip -Force
Set-Location -Path "release\tmp\"
7z a -tzip -y "bfbb.zip" "bfbb"
Set-Location -Path "..\..\"
# Check if the target file exists and remove it
if (Test-Path $apworldOutPath) {
    Remove-Item $apworldOutPath -Force
}
# rename to apworld
Move-Item -Path $apworldOutZip -Destination $apworldOutPath
# clean up
Remove-Item -Recurse -Force -Path $apworldBuildPath


Write-Host "Build script completed!"


