import subprocess


def get_windows_ip():
    try:
        # Executa o comando PowerShell para obter o IP do Windows
        result = subprocess.run(
            [
                "powershell.exe",
                "-Command",
                'Get-NetIPAddress | Where-Object { $_.InterfaceAlias -eq "Ethernet" -and $_.AddressFamily -eq "IPv4" } | Select-Object -ExpandProperty IPAddress',
            ],
            capture_output=True,
            text=True,
        )

        # Verifica se o comando foi executado com sucesso
        if result.returncode != 0:
            raise Exception("Erro ao executar o comando PowerShell")

        # Extrai o endereço IP da saída do comando
        ip_address = result.stdout.strip()
        if not ip_address:
            raise Exception("Não foi possível obter o endereço IP")

        return ip_address

    except Exception as e:
        print(f"Erro: {e}")
        return None


# windows_ip = get_windows_ip()
# if windows_ip:
#     print(f"IP do Windows: {windows_ip}")
# else:
#     print("Não foi possível obter o IP do Windows")
