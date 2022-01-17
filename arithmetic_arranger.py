def arithmetic_arranger(problems, solve=False):
  top_line = []
  middle_line = []
  bottom_line = []
  solution = []
  index = 0
  error = 0
  for problem in problems:
    indiv_nums = problem.split()
    index = index + 1
    if index <= 5:
      i = 1
      try:
        int(indiv_nums[0]) and int(indiv_nums[2])
      except:
        return("Error: Numbers must only contain digits.")
        break
      if len(indiv_nums[0]) > 4 or len(indiv_nums[2]) > 4:
        return("Error: Numbers cannot be more than four digits.")
        break
      else:
        if indiv_nums[1] == '-' or indiv_nums[1] == '+':
          top = indiv_nums[0].rjust(2 + max(len(indiv_nums[0]), len(indiv_nums[2])))
          middle = indiv_nums[1] + " " + indiv_nums[2].rjust(max(len(indiv_nums[0]), len(indiv_nums[2])))
          top_line.append(top)
          middle_line.append(middle)
          bottom_line.append("-" * (2 + max(len(indiv_nums[0]), len(indiv_nums[2]))))
          if solve == True:
            if indiv_nums[1] == '-':
              n = str(int(indiv_nums[0]) - int(indiv_nums[2]))
              sol = n.rjust(2 + max(len(indiv_nums[0]), len(indiv_nums[2])))
              solution.append(sol)
            else:
              n = str(int(indiv_nums[0]) + int(indiv_nums[2]))
              sol = n.rjust(2 + max(len(indiv_nums[0]), len(indiv_nums[2])))
              solution.append(sol)
          else:
            continue
        else:
          return("Error: Operator must be '+' or '-'.")
          break
    else:
      return("Error: Too many problems.")
      break
  seperator = "    "
  if solve == False:
    return (f"""{seperator.join(top_line)}\n{seperator.join(middle_line)}\n{seperator.join(bottom_line)}""")
  else:
    return (f"""{seperator.join(top_line)}\n{seperator.join(middle_line)}\n{seperator.join(bottom_line)}\n{seperator.join(solution)}""")
