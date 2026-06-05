$port = 3000
$dir = "E:\webtanmy"
Write-Host "Starting server at http://localhost:$port/" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop" -ForegroundColor Yellow
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()
while ($listener.IsListening) {
    $ctx = $listener.GetContext()
    $path = $ctx.Request.Url.LocalPath
    if ($path -eq "/") { $path = "/index.html" }
    $file = Join-Path $dir $path.TrimStart("/")
    if (Test-Path $file) {
        $content = [IO.File]::ReadAllBytes($file)
        $ext = [IO.Path]::GetExtension($file)
        $mime = switch ($ext) {
            ".html" { "text/html; charset=utf-8" }
            ".css"  { "text/css" }
            ".js"   { "application/javascript" }
            ".png"  { "image/png" }
            ".jpg"  { "image/jpeg" }
            ".jpeg" { "image/jpeg" }
            ".gif"  { "image/gif" }
            ".svg"  { "image/svg+xml" }
            ".ico"  { "image/x-icon" }
            default { "application/octet-stream" }
        }
        $ctx.Response.ContentType = $mime
        $ctx.Response.OutputStream.Write($content, 0, $content.Length)
    } else {
        $ctx.Response.StatusCode = 404
        $data = [Text.Encoding]::UTF8.GetBytes("404 Not Found")
        $ctx.Response.OutputStream.Write($data, 0, $data.Length)
    }
    $ctx.Response.Close()
}
$listener.Stop()
