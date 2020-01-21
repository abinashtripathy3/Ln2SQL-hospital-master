# import argparse
# 
# from .ln2sql import Ln2sql
# import .connection as conn
# 
# 
# def main():
#     arg_parser = argparse.ArgumentParser(description='A Utility to convert Natural Language to SQL query')
#     arg_parser.add_argument('-d', '--database', help='Path to SQL dump file', required=True)
#     arg_parser.add_argument('-l', '--language', help='Path to language configuration file', required=True)
#     arg_parser.add_argument('-i', '--sentence', help='Input sentence to parse', required=True)
#     arg_parser.add_argument('-j', '--json_output', help='path to JSON output file', default=None)
#     arg_parser.add_argument('-th', '--thesaurus', help='path to thesaurus file', default=None)
#     arg_parser.add_argument('-s', '--stopwords', help='path to stopwords file', default=None)
# 
#     args = arg_parser.parse_args()
# 
#     ln2sql = Ln2sql(
#         database_path=args.database,
#         language_path=args.language,
#         json_output_path=args.json_output,
#         thesaurus_path=args.thesaurus,
#         stopwords_path=args.stopwords,
#     ).get_query(args.sentence)
# 
# if __name__ == '__main__':
#     main()



import argparse
import pprint,os
from ln2sql import Ln2sql
import connection as conn

def print_db_output(out_data):
    for val in out_data:
        pprint.pprint("{0}".format(val))


def write_to_file(fl_path,fl_name,data_content):
	with open(fl_path+'/'+fl_name,'w') as fl_obj:
		fl_obj.write(data_content)
	return


def main():
    #### Connecting to DB to get DDL
    print("\nEstablishing connection from main()")
    sql_conn_obj=conn.DB_Connection()
    #### Getting DDL
    print("\nConnection established.\nExtracting DDL from DB ...")
    ddl_qry='SHOW CREATE TABLE patient;'
    ddl_output=sql_conn_obj.exec_sql(ddl_qry)
#     print("\nLength of ddl_output list is : {0}".format(len(ddl_output[0])))
    new_ddl_output=ddl_output[0][1]+' ;\n'
    print("\nDDL extracted ..\n\nPrinting DDL output ....\nType of output is : {0}".format(type(ddl_output[0])))
#     print_db_output(new_ddl_output[1])
    pprint.pprint(new_ddl_output)
    fl_path=os.getcwd()+'/ln2sql/'
    fl_name='patient.sql'
    write_to_file(fl_path,fl_name,new_ddl_output)    
    arg_parser = argparse.ArgumentParser(description='A Utility to convert Natural Language to SQL query')
    arg_parser.add_argument('-d', '--database', help='Path to SQL dump file', required=True)
    arg_parser.add_argument('-l', '--language', help='Path to language configuration file', required=True)
    arg_parser.add_argument('-i', '--sentence', help='Input sentence to parse', required=True)
    arg_parser.add_argument('-j', '--json_output', help='path to JSON output file', default=None)
    arg_parser.add_argument('-th', '--thesaurus', help='path to thesaurus file', default=None)
    arg_parser.add_argument('-s', '--stopwords', help='path to stopwords file', default=None)

    args = arg_parser.parse_args()

    ln2sql = Ln2sql(
        database_path=args.database,
        language_path=args.language,
        json_output_path=args.json_output,
        thesaurus_path=args.thesaurus,
        stopwords_path=args.stopwords,
    ).get_query(args.sentence)
    data_output=sql_conn_obj.exec_sql(ln2sql)
#     print("\nNow closing connection")
#     data_output=conn.connect_to_db(ln2sql)
#     print("Data Output is :-\n{0}".format(data_output))
    print_db_output(data_output)
    sql_conn_obj.close_connection()

if __name__ == '__main__':
    main()
