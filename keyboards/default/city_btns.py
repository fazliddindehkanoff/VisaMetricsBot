from common.btn_maker import create_keyboard

cities = ["Andijan", "Angren", "Bekobod", "Bukhara", 
          "Chirchiq", "Fergana", "Jizzakh", "Kokand",
          "Margilan", "Namangan", "Navoiy", "Nukus",
          "Olmaliq", "Qarshi", "Samarkand", "Shahrisabz",
          "Tashkent", "Termez", "Urgench"          
        ]

city_btns = create_keyboard(cities, row=True)