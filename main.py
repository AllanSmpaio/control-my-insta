from bs4 import BeautifulSoup


def extrair_usuarios(caminho_arquivo):
    with open(caminho_arquivo, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file,  "html.parser")

        usuarios = set()

        for a in soup.find_all("a"):
            href = a.get("href", "")
            if "instagram.com/" in href:
                username = href.strip("/").split("/")[-1]
                if username:
                    usuarios.add(username)

        return usuarios


def analisar_seguidores():
    try:
        seguidores = extrair_usuarios("followers_1.html")
        seguindo = extrair_usuarios("following.html")

        nao_te_seguem = []
        for u in (seguindo - seguidores):
            if not u.startswith("__deleted__"):
                nao_te_seguem.append(u)

        print(
            f"--- RESULTADO: {len(nao_te_seguem)} pessoas não te seguem de volta ---"
        )
        for usuario in sorted(nao_te_seguem):
            print(f"- @{usuario}")
    except FileNotFoundError:
        print(
            "Erro: Certifique-se de colar os arquivos 'followers_1.html' e 'following.html' na mesma pasta do script."
        )

if __name__ == "__main__":
    analisar_seguidores()