TEST_DATA = [
    {
        "name": "Lenovo LOQ15 2023",
        "data": {
            "year": 2023,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Dell G15 2021",
        "data": {
            "year": 2021,
            "price": 1500,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
]

NEGATIVE_TEST_DATA = [
    {
        "name": "@@@@@@",
        "data": {
            "year": 2023,
            "price": 2000,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "     ",
        "data": {
            "year": 2021,
            "price": 1500,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
]
