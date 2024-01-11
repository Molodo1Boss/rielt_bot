import subprocess

if __name__ == "__main__":
    # Замените пути к вашим парсерам
    parser_paths = [
        "/home/aleksandr/PycharmProjects/Rielt_bot/Pars_cities_run/Chelyabins_pars.py",
        "/home/aleksandr/PycharmProjects/Rielt_bot/Pars_cities_run/ekb_pars.py",
        "/home/aleksandr/PycharmProjects/Rielt_bot/Pars_cities_run/Kaliningrad_pars.py"
    ]

    processes = []

    for parser_path in parser_paths:
        command = ["python3", parser_path]
        process = subprocess.Popen(command, cwd="/home/aleksandr/PycharmProjects/Rielt_bot/Pars_cities_run/")
        processes.append(process)

    # Дождитесь завершения всех процессов
    for process in processes:
        process.wait()
