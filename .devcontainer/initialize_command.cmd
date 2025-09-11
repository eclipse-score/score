REM Create Bazel cache directory if it doesn't exist

set home="%1"
IF not exist "%home%\\.cache\\bazel" ( mkdir "%home%\\.cache\\bazel" )
