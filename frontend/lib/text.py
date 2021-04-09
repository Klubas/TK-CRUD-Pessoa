__texts__ = {
    "PTBR": {
        "error_messages:": {
            "alert": "Alerta",
            "unexpected_error": "Erro inesperado!",
        },

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
        }


    }
}


def _get_texts_(interface, lang="PTBR"):
    texts = __texts__.get(lang).get(interface)
    print(interface)
    print(texts)
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
        return None


def show_message(**kwargs):
    from tkinter import messagebox
    messagebox.showwarning(**kwargs)
