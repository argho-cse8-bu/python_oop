#  List consist of [questions, opt1,opt2,opt3,opt4,correctOpt]
questionList = [
  [
    'Q1.The Government of India and the state government of Assam recently signed a tripartite agreement with which tribal group?',
    'Bodo', 'Kuki', 'Adi', 'Nishi', 1
  ],
  [
    'Q2.‘Navaratnalu – Pedalandariki Illu’ is a welfare scheme of which Indian state, under which 25 lakh house sites are to be distributed at concessional rates to the poor?',
    'Andhra Pradesh', 'Karnataka', 'Telangana', 'Kerala', 1
  ],
  [
    'Q3.Which state/UT has announced \‘Operation SHIELD’\ in containment zones to contain the spread of COVID-19?',
    'New Delhi', 'Telangana', 'Maharashtra', 'Punjab', 1
  ],
  [
    'Q4.Bureau of Police Research and Development (BPRD) is an organisation under which Union Ministry?',
    'Ministry of Home Affairs', 'Ministry of Law and Justice',
    'Ministry of Social Justice and Empowerment', 'Ministry of Defence', 1
  ],
  [
    'Q5.Who is the head of the committee constituted to investigate the fire incident happened in Assam’s Baghjan oil well?',
    'B P Katakey', 'S P Wangdi', 'Siddhanta Das', 'A K Sikri', 1
  ],
  [
    'Q6.What is the name of the mission undertaken by the Indian Navy, to bring back Indian citizens from overseas during the COVID-19 pandemic?',
    'Operation Samudra Setu', 'Operation Sukoon', 'Vande Bharat Mission',
    'Operation Rahat', 1
  ],
  [
    'Q7.Solar Energy Corporation of India is a public sector undertaking working under which Union Ministry?',
    'Ministry of New and Renewable Energy', 'Ministry of Power',
    'Ministry of Coal', 'Ministry of Petroleum and Natural Gas', 1
  ],
  [
    'Q8.Which month of this year has recorded the highest rainfall since 1976?',
    'August', 'July', 'June', 'May', 1
  ],
  [
    'Q9.Which State government’s Skill Development Corporation has partnered with Coursera, to train unemployed youth?',
    'Tamil Nadu', 'Andhra Pradesh', 'Telangana', 'Maharashtra', 1
  ],
  [
    'Q10.Which e-commerce giant has launched a new \‘Fulfilment Centre’\ in Tamil Nadu?',
    'Amazon', 'Flipkart', 'Cloud Tail', 'Snapdeal', 1
  ],
  [
    'Q11.Which social-media platform has launched a search prompt named ‘ThereIsHelp’, to prevent suicide?',
    'Twitter', 'Facebook', 'TikTok', 'WeChat', 1
  ],
  [
    'Q12.A committee has been formed by which Union Ministry for study on origin of Indian culture?',
    'Ministry of Culture', 'Ministry of Home Affairs',
    'Ministry of Housing and Urban Affairs', 'Ministry of Environment', 1
  ],
  [
    'Q13.Which company has bagged the contract to construct the new Parliament building for India?',
    'Tata Projects Limited', 'L&T', 'GMR Infrastructure', 'Adani Group', 1
  ],
  [
    'Q14.What is ‘Ganga Avalokan’, that was seen in news recently?',
    'Campaign', 'Museum', 'Commemorative Stamp', 'Channel', 1
  ],
  [
    'Q15.What is the new ideal weight for adult Indian Men as per National Institute of Nutrition?',
    '65 kg', '75 kg', '85 kg', '90 kg', 1
  ],
  [
    'Q16.The Supreme Court appointed a committee under which eminent person to take steps for preventing stubble burning?',
    'Justice Madan B Lokur', 'Justice Ranjan Gogoi', 'Justice Dipak Misra',
    'Justice Jagdish Singh Khehar', 1
  ]
]
# Code
amount = 0
levels = [
  1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000,
  1250000, 2500000, 5000000, 10000000, 70000000
]

print(
  f"There will be total of {len(questionList)} questions. All the very best!!!\N{grinning face}"
)
for i in range(0, len(questionList)):
  print("\n")
  print(f"The question for Rs.{levels[i]} is:\n")
  print(questionList[i][0])
  print(f"""
    a.{questionList[i][1]}\tb.{questionList[i][2]}
    c.{questionList[i][3]}\td.{questionList[i][4]}
    """)
  option = int(input("Input your selection (1/2/3/4): "))
  if (option == questionList[i][5]):
    print(f"Correct answer, You have won {levels[i]}")
  else:
    print("Wrong Answer\N{grimacing face}\nYou are out of the game!!!")
    break
  if (levels[i] == 10000):
    amount = 10000
  elif (levels[i] == 320000):
    amount = 320000
  elif (levels[i] == 70000000):
    amount = 70000000

print(
  f"\nThank you so much for playing KBC\nCongratulations!!! You have won Rs.{amount} \N{fire}"
)