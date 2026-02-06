from persistence import ExcelPersistence


def main():
    
    # MOCK EXATO DA SAÍDA DA IA (NÍVEL 2)
    mock_ia_output = [
        {
            "emails": ["ibrlojaoficial@gmail.com", "personalizada@importadosbr.net"],
            "telefones": ["(81) 98149-4541"],
            "whatsapp": [],
            "nome_empresa": "Importados BR"
        },
        {
            "emails": [],
            "telefones": [],
            "whatsapp": ["(81) 99515-8125", "(81) 98373-8182"],
            "nome_empresa": "Test"
        }
    ]

    excel = ExcelPersistence()
    excel.save_data(mock_ia_output)


if __name__ == "__main__":
    main()
