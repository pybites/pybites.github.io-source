Title: Use Github to Manage Your Projects in an Agile Way
Date: 2020-04-19 20:50
Category: Tools
Tags: Github, projects, agile, KanBan, productivity, automation, GitLab
Slug: github-projects
Author: Robin Beer
Illustration: github-board.png
Summary: In this article you will learn how to setup a project in GitHub and to use boards to organize you issues using agile methods.

In this article you will learn how to setup a project in GitHub and to use boards to organize your issues using agile methods.

We all have been there, long lists of issues overwhelming our brain.

Wouldn't it be great to organize these issues in a way that simplifies priorization and illustrates progress without having to copy the same issues to Trello?

There is! With `GitHub projects` you can set up boards and use agile methods such as KanBan or Scrum. Let's dive into it!

## Initialization of a GitHub project

First, we create a new GitHub repository to show the process from scratch. If you already have a repository, you can jump to the next paragraph.

First, click on the "+" on the upper right next to your GitHub profile icon to create a new repository:

<img src="images/gh-projects/2020-04-14-22-05-07.png" alt="new repo" style="width: 300px;">

Fill in the form, for example with the title and description that I used to create this article:

![Empty GitHub repository]({filename}/images/gh-projects/2020-04-14-22-02-41.png)

Subsequently, create some dummy issues that describe different tasks that you have to work on.

![Issue Creation on GitHub]({filename}/images/gh-projects/2020-04-14-22-07-58.png)

Your issue list might look like the following:

![GitHub issue list]({filename}/images/gh-projects/2020-04-14-22-16-40.png)

GitHub even suggests to try out `project boards`. But how?

## Creation of new projects

In GitHub, one needs to first create a `project` to subsequently create a `project board`. Therefore, click on the `Try it now!` button or on `Projects` and subsequently on `New project`.

The following window should open:

![GitHub New Project]({filename}/images/gh-projects/2020-04-14-22-21-59.png)

Fill in some creative names, or stay with these great suggestions.

## Creation of project boards

Congratulations, by creating the first `project`, you automatically created a `project board`. It's empty though, so let's populate it.

Therefore, you first have to `Add a column`. I suggest to use the following `columns`:

- `Backlog`: All new issues land here

- `To Do`: Issues that are planned to be worked on soon

- `In Progress`: Issues that are actively being worked on

- `Waiting for Feedback`: Issues that require feedback, to decide whether they are completed

- `Done`: completed issues

These `columns` intuitively visualize the progress of the issues. You can just create them for now and ignore the automation, which we will set up later.

After having created the `columns`, your `project board` should look similar to the following image:

![Empty Project Board]({filename}/images/gh-projects/2020-04-14-22-33-18.png)

But there are still no issues... :(

## Issue allocation to (several) projects

GitHub enables many-to-many relationships between issues and projects. That means, one issue can be attributed to several projects and of course, one project can have infinite (?) issues.

To add issues to this `project`, you have two options:

1. Click on `+ Add cards` and drag and drop the issues to the respective `columns`:
   
   ![Issue allocation to project columns from project board]({filename}/images/gh-projects/2020-04-14-22-40-33.png)
   
2. Open the issues view, open the issues that you want to add to the project in a new tab and click on the settings icon next to `Projects` to select the project you want this issue to be added to:
   
   ![Issue allocation to projects from issues board]({filename}/images/gh-projects/2020-04-14-22-38-22.png)

You might have noticed, that the second step did not add the issues to a `column` yet. You still have to drag and drop it as mentioned in step 1. Or, do you?

## Further useful functionalities

GitHub allows you to **automate** some of the steps described above, to **create labels**, and to **filter the issues** in the `project board`. Let's check out these additional functionalities, that are really useful in everyday project management.

### Manage automation of columns

First let's `manage automation` of the `Backlog` column:

<img src="images/gh-projects/2020-04-14-22-44-25.png" alt="manage automation" style="width: 300px;">

Choose `To Do`, check the shown check boxes as visualized below, and `Update automation`:

<img src="images/gh-projects/2020-04-14-22-45-46.png" alt="manage automation: backlog" style="width: 300px;">

Now, if you go back to the issues view and assign the issue to the project, the issue will be automatically added to the `Backlog` column.

Similarly, `Update automation` for the `column "Done"`, such that merged PRs and closed issues are automatically added to the `column "Done"`. Additionally, you might want to add automation to the `column "In Progress"`, if issues or PRs are reopened.

### Create issue labels

To visualize priority implicitly, the issues can be sorted according to their priority (high position = high priority) within their `columns`.

Additionally, issue labels can be created to visualize priority explicitly. Therefore, click on one of the issue titles and in the sidebar that opens to the right, click on the settings icon in `Labels` and type in `high priority`.

Now, you should be able to `Create new label "high priority"`. Alternatively, you can `Edit labels`.

<img src="images/gh-projects/2020-04-14-23-00-41.png" alt="create new label" style="width: 300px;">

Now, your project board might already look more colorful - and more neat. 👌🏻

![Project view with labels]({filename}/images/gh-projects/2020-04-14-23-05-55.png)

### Filter project board view

Another useful functionality, once the project board gets busy, is to filter the issues.

For example, you might want to see all issues assigned to you or to a specific milestone. Or all issues, that have high priority. Therefore, click on the search field `Filter cards` and type in exactly `label:"high priority"`, such that the project board should change as follows:

![Filtered project view]({filename}/images/gh-projects/2020-04-14-23-08-26.png)

## Summary & Conclusion

In this article, we have checked out how to use GitHub's `project boards` to organize your issues into `columns`.

Therefore, we have created `projects` and assigned the issues to several projects. Using the columns `Backlog`, `To Do`, `In Progress`, `Waiting for Feedback` and `Done`, we can now intuitively visualize the progress of the issues.

Additionally, we can visualize the priority of the issues implicitly using the position (highest = highest priority) as well as explicitly using labels `high priority` and `low priority`.

Furthermore, we have `managed automation` to automatically move issues to `Backlog` when they are added to the project and `Done` when they are closed.

What are you waiting for? Get back control over all the open issues and manage them using `GitHub projects`!

Whether you use the `project board` with [Scrum](https://www.scrum.org/resources/what-is-scrum) or [KanBan](https://www.atlassian.com/agile/kanban), it will simplify priorization and visualization of progress.

This can also be a game changer in communicating workload and available ressources with your colleagues, your mentors or your boss.

---

You like the idea of issue organization into boards, but are using GitLab?

Check out [my blog](https://www.robin-beer.de/), instructions for GitLab will follow soon!

Cheers! 

-- [Robin](pages/guests.html#robinbeer)
