import gsheets as gs
from datetime import datetime as dt

from gsheets import updateGSheets

vocabular = {'Первое практическое занятие по Python':'Первая методичка',
'Нулевое практическое занятие по Python':'Нулевая методичка',
'Второе практическое занятие по Python':'Вторая методичка',
'Третье практическое занятие по Python':'Третья методичка',
'Четвёртое практическое занятие по Python':'Четвёртая методичка',
'Упражнение 1':'Упражнение 1',
'Упражнение 2':'Упражнение 2',
'Упражнение 3':'Упражнение 3',
'Упражнение 4':'Упражнение 4',
'Упражнение 5':'Упражнение 5',
'Упражнение 6':'Упражнение 6',
'Упражнение 7':'Упражнение 7',
'Упражнение 8':'Упражнение 8',
'Упражнение 9':'Упражнение 9',
'Упражнение 10':'Упражнение 10'}

def aggregateTries(tries, row, test_name):
    tries[test_name]['question'] = row['question']
    tries[test_name]['step'] = str(abs(int(row['step'])))
    tries[test_name]['status'] = row['status']
    tries[test_name]['time'] = row['time']
    tries[test_name]['attempt_id'] = row['attempt_id']
    tries[test_name]['question_usage_id'] = row['question_usage_id']

def main():
    performance = gs.read_sheet(gs.table, 'PerformanceTuesday',)
    # for el in performance:
    #     print(el)
    data = gs.read_sheet(gs.table, 'Data', index = 1)
    # for el in data:
    #     print(el)
    for st in performance:
        tries = {} # test_name;;question: {}
        res = {}
        # print(st['FIO'])
        for row in data:
            if row['FIO'] == st['FIO']:
                test_name = row['test_name']+';;'+row['question']
                # print(test_name)
                #Второе практическое занятие по Python;;3
                if not test_name in tries:
                    tries[test_name] =  {'question': '',
                                         'step': '0',
                                         'status': '',
                                         'time': '0',
                                         'attempt_id': '0',
                                         'question_usage_id': '0'}
                    aggregateTries(tries, row, test_name)
                elif tries[test_name]['status'] != 'complete':
                    aggregateTries(tries, row, test_name)
        for testQ, val in tries.items():
            test_name = testQ.split(';;')[0]
            if not test_name in res:
                res[test_name] = {'res': [],
                     'question': '',
                     'step': '0',
                     'status': '',
                     'time': '0',
                     'attempt_id': '0',
                     'question_usage_id': '0'}
            if val['status'] != 'complete':
                res[test_name]['res'] += [val['question']+'.'+val['step']]
                aggregateTries(res, val, test_name)
        for test in res:
            perf_test_name = vocabular[test]
            if len(res[test]['res']) != 0:
                st[perf_test_name] = f'=ГИПЕРССЫЛКА("https://moodle.surgu.ru/mod/quiz/review.php?attempt={res[test]['attempt_id']}#question-{res[test]['question_usage_id']}-{res[test]['question']}"; "{', '.join(res[test]['res'])}")'
            else:
                st[perf_test_name] = "'+"
        # print(st)
    gs.updateGSheets(gs.table, 'PerformanceTuesday', performance, start_row=3)

if __name__ == '__main__':
    main()