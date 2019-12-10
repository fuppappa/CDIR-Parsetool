def getColors():
    ecp = "\033["
    return {
        "GRAY": ecp + str(90) + ";2m",
        "RED": ecp + str(91) + ";2m",
        "GREEN": ecp + str(92) + ";2m",
        "YELLOW": ecp + str(33) + ";2m",
        "BLUE": ecp + str(94) + ";2m",
        "PURPLE": ecp + str(95) + ";2m",
        "CYAN": ecp + str(96) + ";2m",
        "GRAY_E": ecp + str(90) + ";1m",
        "RED_E": ecp + str(91) + ";1m",
        "GREEN_E": ecp + str(92) + ";1m",
        "YELLOW_E": ecp + str(33) + ";1m",
        "BLUE_E": ecp + str(94) + ";1m",
        "PURPLE_E": ecp + str(95) + ";1m",
        "CYAN_E": ecp + str(96) + ";1m",
        "GRAY_U": ecp + str(90) + ";4m",
        "RED_U": ecp + str(91) + ";4m",
        "GREEN_U": ecp + str(92) + ";4m",
        "YELLOW_U": ecp + str(33) + ";4m",
        "BLUE_U": ecp + str(94) + ";4m",
        "PURPLE_U": ecp + str(95) + ";4m",
        "CYAN_U": ecp + str(96) + ";4m",
        "CLEAR": ecp + str(0) + "m"
    }
