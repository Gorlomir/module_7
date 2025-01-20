def format_strings(team1_num, team2_num, score_1, score_2, team1_time, team2_time, tasks_total, time_avg,
                   challenge_result):
    percent_string = f"В команде 'Мастера кода' участников: {team1_num} ! " # Использование %
    both_teams_string = f"Итого сегодня в командах участников: {team1_num} и {team2_num} !"

    data_2_string = f"Команда 'Волшебники данных' решила задач: {score_2:.0f} !" # Использование .format()
    time_2_string = f" Волшебники данных решили задачи за {team2_time:.2f}s !"

    score_string = f"Команды решили {score_1:.0f} и {score_2:.0f} задач." # Использование f-строк
    result_string = f"Результат битвы: {challenge_result}"
    total_tasks_string = f"Сегодня было решено {tasks_total:.0f} задач, в среднем по {time_avg:.1f} секунд на задачу!"

    return {
        "percent": percent_string,
        "both_teams": both_teams_string,
        "data_2": data_2_string,
        "time_2": time_2_string,
        "score": score_string,
        "result": result_string,
        "total_tasks": total_tasks_string
    }

if __name__ == "__main__":
    team1_num = 6
    team2_num = 6
    score_1 = 40
    score_2 = 42
    team1_time = 1552.512
    team2_time = 2153.31451
    tasks_total = 82
    time_avg = 45.2
    challenge_result = 'Победа команды Волшебники данных!'

    formatted_strings = format_strings(team1_num, team2_num, score_1, score_2,
                                       team1_time, team2_time, tasks_total, time_avg, challenge_result)

    for key, value in formatted_strings.items():
        print(f"{key}: {value}")