def get_middle_tree_chars(sample_str):
	middle_index=int(len(sample_str)/2)
	print("original string is", sample_str)
	middle_three=sample_str[middle_index-1:middle_index+2]
	print("middle three chars are",middle_three)
get_middle_tree_chars("sakjdaskjdlk")
get_middle_tree_chars("abcds")