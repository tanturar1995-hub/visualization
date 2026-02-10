# Data Visualization

## Assignment 2: Good and Bad Data Visualization

### Requirements:

- Data visualizations are important tools for communication and convincing; we need to be able to evaluate the ways that data are presented in visual form to be critical consumers of information 
- To test your evaluation skills, locate two public data visualizations online, one good and one bad  
    - You can find data visualizations at https://public.tableau.com/app/discover or https://datavizproject.com/, or anywhere else you like! 
- For each visualization (good and bad):  
    - Explain (with reference to material covered up to date, along with readings and other scholarly sources, as needed) why you classified that visualization the way you did.
      ```
      Gapminder World Health Chart — Good

    Visualization: Gapminder World Health Chart (income vs life expectancy over time) Link: https://www.gapminder.org/fw/world-health-chart/

    Why I classified this as “good” : This visualization is a strong example of “good” data visualization because it fits the purpose (showing relationships and change over time), the audience (broad public), and the medium (interactive web) as we studied in our lecture 04_choosing_the_right_visualization. It communicates a clear story: how life expectancy relates to income, and how countries move through time. The core view is a 2D scatterplot (a familiar chart type), which helps limit extraneous cognitive load compared to rare chart forms. 

    The most important quantities (income and life expectancy) are encoded as position on a common scale, which our notes describe as more accurate and less cognitively demanding than interpreting areas/relationships alone. It also supports trust: the interface is clean and “data-first,” aligning with course discussion of how 2D, clean layouts, and sourcing conventions influence perceived credibility (“perceived factual basis” and “provenance rhetoric”). 

    Finally, it performs well on the course’s three evaluation dimensions—aesthetic, substantive, and perceptual—because it is readable, honest to the data structure, and makes the message understandable. 

    ------------------

    Visualization: “2012 Presidential Run” pie chart by Fox News (often reposted as an example of misleading graphics). Link: https://www.datavis.ca/gallery/images/pies/FoxNews-GOP.png

    Why I classified this as “bad”: First, it uses the wrong chart form for the meaning of the data. A pie chart encodes “parts of a whole,” but the displayed values (e.g., 70%, 63%, 60%) are not parts of a single whole; they are separate percentages that can exceed 100% when combined. This violates our course emphasis that chart choice shapes interpretation and should match the message and data structure (Reference: 04_choosing_the_right_visualiztion). Second, the graphic is perceptually unreliable: pie slices require comparing angles/areas, which is generally less accurate than comparing positions along a common scale (e.g., bars or dots). This connects to the course discussion of cognitive load and the idea that area/relational judgments increase extraneous cognitive load compared to position-based decoding. 

    Third, it lacks essential context and transparency. The chart does not clearly state the question wording or whether responses overlap (“select all that apply” vs “choose one”). That undermines reproducibility: work should be checkable because data and methods are available (Reference: lecture 03_reproducible).

    Finally, the styling choice is a problem: the course explicitly warns “No 3D without cause,” because 3D effects add distortion without adding information. This also connects to the course’s discussion (via Data Feminism) that visualization is not neutral—design choices can push a narrative while appearing “data-driven.” 

      ```
    - How could this data visualization have been improved?  
      ```
    How it could be improved "good example" :

    1. Accessibility: do not rely only on colour to encode region; add patterns/labels or other cues ( Reference: lecture notes 07_accessible_data_visualization )

    2. Provide built-in text descriptions / alt-text style summaries for screen-reader users (what the chart shows + key trends). 


    How it could be improved "bad example" :

    1. Replace the pie chart with a bar chart or dot plot (common baseline), so each percentage is shown independently and accurately.

    2. Add clear metadata: survey question, whether multiple selections were allowed, sample size, date, and population (supports transparency and reproducibility). 

    3. Apply accessibility checks (contrast, readable labels, don’t rely on colour alone).



      
      ```
- Word count should not exceed (as a maximum) 500 words for each visualization (i.e. 
300 words for your good example and 500 for your bad example)

### Why am I doing this assignment?:

- This assignment ensures active participation in the course, and assesses the learning outcomes
* Apply general design principles to create accessible and equitable data visualizations
* Use data visualization to tell a story

### Rubric:

| Component               | Scoring   | Requirement                                                 |
|-------------------------|-----------|-------------------------------------------------------------|
| Data viz classification and justification | Complete/Incomplete | - Data viz are clearly classified as good or bad<br />- At least three reasons for each classification are provided<br />- Reasoning is supported by course content or scholarly sources |
| Suggested improvements  | Complete/Incomplete | - At least two suggestions for improvement<br />- Suggestions are supported by course content or scholarly sources |

## Submission Information

🚨 **Please review our [Assignment Submission Guide](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md)** 🚨 for detailed instructions on how to format, branch, and submit your work. Following these guidelines is crucial for your submissions to be evaluated correctly.

### Submission Parameters:
* Submission Due Date: `23:59 - 01/26/2026`
* The branch name for your repo should be: `assignment-2`
* What to submit for this assignment:
    * This markdown file (assignment_2.md) should be populated and should be the only change in your pull request.
* What the pull request link should look like for this assignment: `https://github.com/<your_github_username>/visualization/pull/<pr_id>`
    * Open a private window in your browser. Copy and paste the link to your pull request into the address bar. Make sure you can see your pull request properly. This helps the technical facilitator and learning support staff review your submission easily.

Checklist:
- [ ] Create a branch called `assignment-2`.
- [ ] Ensure that the repository is public.
- [ ] Review [the PR description guidelines](https://github.com/UofT-DSI/onboarding/blob/main/onboarding_documents/submissions.md#guidelines-for-pull-request-descriptions) and adhere to them.
- [ ] Verify that the link is accessible in a private browser window.

If you encounter any difficulties or have questions, please don't hesitate to reach out to our team via our Slack. Our Technical Facilitators and Learning Support staff are here to help you navigate any challenges.
