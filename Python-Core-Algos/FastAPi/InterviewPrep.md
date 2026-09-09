# Prep

## Python Fundamentals (High Probability)

What is the difference between a list and a tuple?

**A tuple is a immutable where as a list can be added to or removed**

What is a dictionary comprehension?

**Setting up a dictionary inline**

What is the difference between == and is?

**'==' Comapare the value of to objects 'is' compares if object point to the same location in memory**

What are generators?

**Functions which use a yeild to return a iterator. When called preducing values one at a time**
**Useful because they generate values in execution time and doesnt save items to memory conserve memory**

How would you ensure that the code you write is maintainable and meets quality standards, especially as part of a team?

**Keep the code well documented via comments within a code. Use a teams style document if there is one. Write unit tests even if they're small**

```def add_items(items=[]):
    items.append("new")
    return items

print(add_items())
print(add_items())

['new']
['new', 'new']

```

**The default argument is mutable and persists across calls.**
**To fix this you will have assign none to items and initialize it in the first line**

Could you explain what asynchronous programming is in Python and give me a simple use case where you’d prefer async over sync?

**Async programming allows you to pause operations to let other tasks run during the down time**
**You would use Async to handle multiple api calls at once**

Can you briefly tell me how you’d manage version control in a team environment when collaborating on the same codebase?

**You could use different version control software such as Git or svn. When changes have been made or tested you conduct a pull request, You ask teams to pull frequently, ask for code reviews and hopefully if done right the merge conflicts are little to none**

What is a pull request?

**Wheb you alert others in a team that you have completed a task/implemented a feature and you request the team to sync to the latest version**

SQL Join?

**SQL join is when combine two different tables based on the criteria of another**

**Inner join is when: You return a record that has matching values in both tables**
**Left Join: When you return all record from the left table (Table in the from) and the matching values in the right**
**Right Join: When you return all the records in the right table and the matching values in the left(Table in the from)**
**Full Join: When you return all the records when there is a match in both tables**