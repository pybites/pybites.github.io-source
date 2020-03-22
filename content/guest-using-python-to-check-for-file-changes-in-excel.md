Title: Using Python to Check for File Changes in Excel
Date: Date: 2020-03-22 12:59
Category: Tools
Tags: pandas, excel, os
Slug: using-python-to-check-for-file-changes-in-excel
Authors: Ryan Cheley
summary: TBD
cover: images/featured/pb-guest.png


<!-- Indexes are always a good start! -->
## Index
* [The Problem](#problem)
* [The Solution](#solution)
	
<a name="problem"></a>
## The Problem 

Data exchange in healthcare is ... harder than it needs to be. Not all partners in the healthcare arena understand and use technology to it's fullest beenfit. 

Take for example several health plans which want data reported to them for CMS (Centers for Medicare and Medicaid Services) regulations. They will ask their 'delegated' groups to fill out ann excel file. As in, they expect you will *actually* fill out an excel file, either by manually entering the data OR by potentially copying and asting your data into their excel file. 

They will also, quite frequently, change their mind on what they want AND the order in which they want the data to appear in their excle file. But there's no change log to tell you what (if anything has changed). All that you will get is an email which states, "Here's the new template to be used for report XYZ" ... even if this 'new' report is the same as the last one that was sent. 

Some solutions might be to use versioning software (like Git) but all they will do is tell you that there is a difference, not *what* the difference is. For example, when looking at a simple excel file added to git and using `git diff` you see:

```
diff --git a/Book3.xlsx b/Book3.xlsx
index 05a8b41..e96cdb5 100644
Binary files a/Book3.xlsx and b/Book3.xlsx differ
```

This has been a giant pain in the butt for a while, but with the recent shelter-in-place directives, I have a bit more time on the weekends to solve these kinds of problems. 

<a name="solution"></a>
## The Solution

Why Python of Course! 

Only two libraries are needed to make the comparison: (1) os, (2) pandas

The basic idea is to:

1. Load the files
2. use pandas to compare the files
3. write out the differences, if they exist

### Load the Files

The code below loads the necessary libraries, and then loads the excel files into 2 pandas dataframes. One thing that my team has to watch out for are tab names that have leading spaces that aren't easy to see inside of excel. This can cause all sorts of nightmares from a troubleshooting perspective.

```

import os
import pandas as pd

file_original = os.path.join(\\path\\to\\original\\file, original_file.xlsx)
file_new = os.path.join(\\path\\to\\new\\file, new_file.xlsx)

sheet_name_original = name_of_sheet_in_original_file
sheet_name_new = name_of_sheet_in_new_file

df1 = pd.read_excel(file_original, sheet_name_original)
df2 = pd.read_excel(file_new, sheet_name_new)


```

### Use Pandas to compare

This is just a one liner, but is super powerful. Pandas DataFrames have a method to see if two frames are the same. So easy!

```

data_frame_same = df1.equals(df2)

```

### Write out the differences if they exist:


First we specify where we're going to write out the differences to. We use `w+` because we'll be writing out to a file AND potentially appending, depending on differences that are found. The `f.truncate(0)` will clear out the file so that we get just the differences on this run. If we don't do this then we'll just append to the file over and over again ... and that can get confusing.

```

f.open(\\path\\to\\file\\to\\write\\differences.txt, 'w+')
f.truncate(0)


```

Next, we check to see if there are any differences and if they are, we write a simple message to our text file from above:

```

if data_frame_same:
	f.write('No differences detected')

```

If differences are found, then we loop through the lines of the file, finding the differences and and writing them to our file:


```

else:
	f.write('*** WARNING *** Differences Found\n\n')
	for c in range(max(len(df1.columns), len(df2.columns))):
		try:
			header1 = df1.columns[c].strip().lower().replace('\n', '')
			header2 = df2.columns[c].strip().lower().replace('\n', '')
			if header1 == header2:
				f.write(f'Headers are the same: {header1}\n')
			else:
				f.write(f'Difference Found: {header1} -> {header2}\n')
		except:
			pass

f.close()

```

The code above finds the largest column header list (the file may have had a new column added) and uses a `try/except` to let us get the max of that to loop over. 

Next, we check for differences between `header1` and `header2`. If they are the same, we just write that out, if they aren't, we indicate that `header1` was transformed to `header2`

A sample of the output when the column headers have changed is below:

```
*** WARNING *** Differences Found

Headers are the same: beneficiary first name
...
Difference Found: person who made the request -> who made the request?
...

```

## Future Enhancements

In just using it a couple of times I've already spotted a couple of spots for enhancements:

1. Use `input` to allow the user to enter the names/locations of the files
2. Read the tab names and allow user to select from command line


## Conclusion

I'm looking forward to implementing the enhancemnts mentioned above to make this even more user friendly. In the mean time, it'll get the job done and allow someone on my team to work on something more interesting than comparing excel files to try (and hopefully find) differences.

-- [Ryan](pages/guests.html#ryancheley)
