Title: The Pythonic Fast Lane, Digest of a 30 Min Mentoring Session
Date: 2020-02-12 13:00
Category: Coaching
Tags: mentoring, developer mindset, requests, APIs, environment variables, kwargs, f-strings, pdb
Slug: python-mentoring-session
Authors: Bob
Summary: The other day I had an awesome mentoring session with a beginner Pythonista, amazing what 30 min of screen sharing can do. Read on to learn more ...
cover: images/featured/pb-article.png

The other day I had an awesome mentoring session with a beginner Pythonista, amazing what 30 min of screen sharing can do. Read on to learn more ...

There was a clear goal: get data from an API so I taught the following:

- First make a virtual environment, activate it and `pip install requests`.

- Open a `script.py`, import the library and define the API endpoint.

- Use an _f-string_ to embed variables into the API endpoint.

- Use `requests.get` with the endpoint URL and its _kwargs_ to send HTTP Headers / secret auth token (more below).

- How to load in the token from the environment (`os.getenv`) to hide it from the source (we added it to `venv/bin/activate`).

- Use pdb to inspect the response (one of my favorites).

- How to read code of an external library.

- And more ...

Feeling as excited as we were hacking this together?

Well, this was _only_ the technical part!

What was more interesting was teaching the PROCESS:

- He saw me use the tools of a professional environment: venv, pip, requests, coding in vim, etc.

- He got an idea how I approached this problem, my thought process. This is **golden** when you get started.

- I did not write a function. I just got something to work first (drop perfectionism).

- We hit a `401` which meant we were not doing authentication right so we advanced from there (quickly iterate).

- Similarly we hardcoded the token in the code to get it working, later we pulled it into an env variable.

- Sending HTTP headers with requests was not something I knew from memory so I had to Google it and landed on Stackoverflow. As a developer you keep learning and googling, you just come better at how to look. He made me aware of this.

- It was nice to teach the bare minimum but leave enough up to a challenge for him. Good mentoring is to give mentees just enough to get going, but they have to do the work. You just guide them.

- Although he was a beginner, he saw how I used `pdb` to inspect variables, a powerful skill.

- I typed help in pdb (duh), then in the REPL, but ended up going to [requests' source code](https://github.com/psf/requests/blob/master/requests/api.py) which he really enjoyed. I told him that "if there was one thing I would have done earlier as a becoming programmer ...".

- I hardcoded a variable and added a `TODO` to make it a command line arg later.

Invaluable stuff. Coaching has a clear win/win here:

- Mentees win because they can focus their efforts.

- Mentors win by better understanding the concepts at hand, gaining tactics for effective knowledge transfer, and learning about common knowledge gaps and roadblocks.

Cliche or not, but **the best way to learn is to teach**.

Have you had a similar experience, be it as a mentee or a mentor? Share it in the comments below ...

Keep Calm and Code in Python!

-- Bob
