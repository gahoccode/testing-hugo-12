@echo off
REM Script to switch Hugo themes
if "%1"=="" (
  echo Please provide a theme name. Available themes:
  echo   paper
  echo   papermod
  echo   typo
  echo   mini
  echo   serif
  echo   console
  exit /b
)

set THEME=%1

if "%THEME%"=="paper" (
  hugo server -t paper
) else if "%THEME%"=="papermod" (
  hugo server -t PaperMod
) else if "%THEME%"=="typo" (
  hugo server -t typo
) else if "%THEME%"=="mini" (
  hugo server -t mini
) else if "%THEME%"=="serif" (
  hugo server -t serif
) else if "%THEME%"=="console" (
  hugo server -t hugo-theme-console
) else (
  echo Unknown theme: %THEME%
  echo Available themes:
  echo   paper
  echo   papermod
  echo   typo
  echo   mini
  echo   serif
  echo   console
)
