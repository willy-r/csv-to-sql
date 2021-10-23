import os
import csv
import sys


def csv_to_sql(csv_file: str, table_name: str) -> str:
    with open(csv_file, newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)

        # Pula o cabeçalho.
        next(reader)

        rows_inserts = ''
        for row in reader:
            # Trata alguns casos especiais.
            p_name = row[2].replace("'", "\\\'")  # Se tiver aspas simples, escapa ela.

            # Aqui é onde a magia acontece, baseando-se na quantidade e no tipo de colunas
            # que a tabela tem. Alterar conforme necessidade, e tratar casos especiais.
            row_str = f"{row[0]}, {row[1]}, '{p_name}', '{row[3]}', {row[4]}, {row[5]}, {row[6]}, {row[7]}, {row[8]}, {row[9]}, {row[10]}, {row[11]}, {row[12]}, {row[13]}, {row[14]}, {row[15]}, {row[16]}, {row[17]}, {row[18]}, {row[19]}, {row[20]}, {row[21]}"

            rows_inserts += f"INSERT INTO {table_name} VALUES ({row_str});\n"

    return rows_inserts


def save_to_sql(dest_path: str, sql: str) -> str:
    head_tail = os.path.split(dest_path)
    dirs = head_tail[0] if head_tail[0] != '' else 'data'

    if not os.path.isdir(dirs):
        try:
            os.makedirs(dirs, exist_ok=True)
        except Exception as err:
            print('Coé, deu erro, se liga:', err)
            sys.exit()

    full_path = os.path.join(dirs, head_tail[1])

    with open(full_path, 'w', encoding='utf-8') as f_obj:
        f_obj.write(sql)

    return full_path


if __name__ == '__main__':
    try:
        path_from = sys.argv[1]
        path_to = sys.argv[2]
    except IndexError:
        print('Deu erro irmão, especifica arquivos aí')
        sys.exit()

    inserts = csv_to_sql(path_from, 'detalhes_jogo')
    path_saved = save_to_sql(path_to, inserts)

    print('Arquivo SQL salvo em:', path_saved)
