# from seven_parc import Parser
# import time


# def main():
#     parser = Parser('https://7745.by/catalog/obogrevateli')
#     parser.accept_cookie()
#     try:
#         while True:
#             time.sleep(1)
#             parser.electro_choice()
#             print(len(parser.links_list))
#             time.sleep(1)
#             parser.go_to_the_next_page()

#     except Exception as e:
#         print(e)

#     parser.get_info()
#     print(parser.info_list)
#     parser.creating_csv_file()


# if __name__ == "__main__":
#     main()

# from seven_parc import Parser
# import time


# def main():
#     parser = Parser('https://7745.by/catalog/obogrevateli')
#     parser.accept_cookie()
#     try:
#         while True:
#             time.sleep(1)
#             parser.electro_choice()
#             print(len(parser.links_list))
#             time.sleep(1)
#             parser.go_to_the_next_page()

#     except Exception as e:
#         print(e)

#     parser.get_info()
#     print(parser.info_list)
#     parser.creating_csv_file()


# if __name__ == "__main__":
#     main()

from seven_parc import Parser
import time


def main():
    # Твой класс сам откроет нужное окно браузера здесь
    parser = Parser('https://7745.by/catalog/obogrevateli')
    
    parser.accept_cookie()
    time.sleep(1)
    
    try:
        parser.electro_choice()
        time.sleep(1.5)
        
        parser.power()
        time.sleep(2)
        
        parser.power_second()
        time.sleep(1)

        parser.mange()
        time.sleep(2.5)

        parser.show_product()
        time.sleep(1)
    except Exception:
        pass

    try:
        while True:
            time.sleep(1)
            print(len(parser.links_list))
            time.sleep(1)
            parser.go_to_the_next_page()

    except Exception as e:
        print(e)

    parser.get_info()
    print(parser.info_list)
    parser.creating_csv_file()


if __name__ == "__main__":
    main()
