__texts__ = {
    "PTBR": {
        "dbconfig": {
            "env_config": "Configuração de ambiente",
            "confirm": "Confirmar",
            "close": "Fechar",
            "cancel": "Cancelar",
            "hostname": "Endereço",
            "port": "Porta",
            "username": "Usuário",
            "password": "Senha"
        },

        "crud_person": {
            "new_person": "Cadastrar Pessoa",
            "name": "Nome",
            "documents": "Documentos",
            "tax_id": "CPF",
            "document": "RG",
            "contact_info": "Contato",
            "email": "Email",
            "phone_number": "Telefone",
            "addresses": "Endereços",
            "address": "Endereço",
            "street_name": "Logradouro",
            "address_number": "Número",
            "district": "Bairro",
            "complement": "Complemento",
            "country": "País",
            "delete_person": "Excluir cadastro",
            "required_fields": "Campos obrigatórios não preenchidos."
        },

        "find": {
            "find": "Localizar",
            "person": "Pessoa",
            "person_not_found": "Pessoa não encontrada!",
            "tax_id_not_supplied": "Informe um CPF."
        },

        "main_window": {
            "find_person": "Localizar Pessoa",
            "new_person": "Cadastrar Pessoa",
            "env_config": "Configuração de ambiente",
            "alert": "Alerta",
            "unexpected_error": "Erro inesperado!",
            "required_fields": "Campos obrigatórios não preenchidos.",
            "person_not_found": "Pessoa não encontrada!",
            "tax_id_not_supplied": "Informe um CPF."
        }


    }
}


def _get_texts_(interface, lang="PTBR"):
    texts = __texts__.get(lang).get(interface)
    return texts


def get_string(texts=None, key=None):
    try:
        if texts is not None:
            text = texts.get(key)
        else:
            text = key
        return text
    except Exception as e:
        print(str(e))
        return key


def show_message(**kwargs):
    from tkinter import messagebox
    title = kwargs.get('title')
    message = kwargs.get('message')

    texts = _get_texts_(interface='main_window', lang='PTBR')

    title = get_string(texts=texts, key=title)
    message = get_string(texts=texts, key=message)

    kwargs.pop('title')
    kwargs.pop('message')

    messagebox.showwarning(title=title, message=message)
