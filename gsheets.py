from gspread import Client, Spreadsheet, Worksheet, service_account


def client_init_json() -> Client:
    """Создание клиента для работы с Google Sheets."""
    return service_account(filename='sa\\example2-442913-99cf4051b1c6.json')



def get_table_by_id(client: Client, table_url):
    """Получение таблицы из Google Sheets по ID таблицы."""
    return client.open_by_key(table_url)

def test_get_table(table_key: str):
    """Тестирование получения таблицы из Google Sheets."""
    client = client_init_json()
    table = get_table_by_id(client, table_key)
    # print('Инфо по таблице по id: ', table)
    return table

def get_worksheet_info(table: Spreadsheet) -> dict:
    """Возвращает количество листов в таблице и их названия."""
    worksheets = table.worksheets()
    worksheet_info = {
        "count": len(worksheets),
        "names": [worksheet.title for worksheet in worksheets]
    }
    return worksheet_info

def read_sheet(table: Spreadsheet, sheet_name: str, index = 2) -> list[dict]:
    """
    Извлекает данные из указанного листа таблицы Google Sheets и возвращает список словарей.

    :param table: Объект таблицы Google Sheets (Spreadsheet).
    :param sheet_name: Название листа в таблице.
    :return: Список словарей, представляющих данные из таблицы.
    """
    worksheet = table.worksheet(sheet_name)
    headers = worksheet.row_values(index)  # Первая строка считается заголовками

    data = []
    rows = worksheet.get_all_values()  # Начинаем считывать с второй строки
    rows = rows[index:]

    for row in rows:
        row_dict = {headers[i]: value for i, value in enumerate(row)}
        data.append(row_dict)

    return data

def updateGSheets(table: Spreadsheet, title: str, data: list[dict], start_row: int = 2) -> None:
    """
    Добавляет данные на рабочий лист в Google Sheets.

    :param table: Объект таблицы (Spreadsheet).
    :param title: Название рабочего листа.
    :param data: Список словарей с данными.
    :param start_row: Номер строки, с которой начнется добавление данных.
    """
    worksheet = table.worksheet(title)

    headers = data[0].keys()
    end_row = start_row + len(data) - 1
    end_col = chr(ord('A') + len(headers) - 1)

    cell_range = f'A{start_row}:{end_col}{end_row}'
    cell_list = worksheet.range(cell_range)

    flat_data = []
    for row in data:
        for header in headers:
            flat_data.append(row[header])

    for i, cell in enumerate(cell_list):
        cell.value = flat_data[i]

    worksheet.update_cells(cell_list, value_input_option = 'user_entered')

# table_name = "https://docs.google.com/spreadsheets/d/1-EOZVonyvq4JEh_-d0kuiUecqsPwRvTPTwd2qb_C5yU/edit?gid=1869783570#gid=1869783570"
table_id = "1-EOZVonyvq4JEh_-d0kuiUecqsPwRvTPTwd2qb_C5yU"
table = test_get_table(table_id)

if __name__ == '__main__':
    # Получаем информацию о листах
    info = get_worksheet_info(table)

    print(f"Количество листов: {info['count']}")
    print("Названия листов:")
    for name in info['names']:
        print(name)
    # print()
    print(read_sheet(table, sheet_name='Performance'))