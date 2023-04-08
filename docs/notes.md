# notes

- change powershell script execution permissions. 2nd line undoes it.
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
Set-ExecutionPolicy Restricted```

Removed methods:
`__del__()` methods dont work with async context managers
`fileno()`
`get_socket()`
