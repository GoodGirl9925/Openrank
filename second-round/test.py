overall_trustworthy_full_seq = [1, 3, 2, 5, 4]
overall_trustworthy_rateOfChange_full_seq = []

if len(overall_trustworthy_full_seq) > 0:
    overall_trustworthy_rateOfChange_full_seq.append(0)
    for i in range(1, len(overall_trustworthy_full_seq)):
        prev = overall_trustworthy_full_seq[i - 1]
        current = overall_trustworthy_full_seq[i]
        rate_of_change = (current - prev) / prev
        overall_trustworthy_rateOfChange_full_seq.append(rate_of_change)

print(overall_trustworthy_rateOfChange_full_seq)