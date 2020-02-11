---
name: Ayanna
surname: St. Rose
position: "PhD Student"
address: "Department of Biology, University of Arkansas"
phone: +1 479 575 0000
www: stroseayanna.wixsite.com
email: "astrose@uark.edu"
twitter: a_st_rose
github: astrose
linkedin: Ayanna St. Rose
date: "`r format(Sys.time(), '%B %Y')`"
output: vitae::hyndman
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, warning = FALSE, message = FALSE)
library(vitae)
```

# Dissertation Title

Investigating the spatio-temporal effects of increasing greenhouse gases and climate change from leaf to forest landscape level.

# Education

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
  "PhD Biology", "2019- 24", "University of Arkansas", "Fayetteville, Arkansas",
  "MSc. Statistical Analysis", "2019- 21", "University of Arkansas", "Fayetteville, Arkansas",
  "BSc Biology", "2015- 19", "University of Arkansas", "Fayetteville, Arkansas",
   "AS Biology & Physics", "2012- 14", "Dominica State College", "Roseau, Dominica"
) %>% 
  detailed_entries(Degree, Year, Institution, Where)

```

# Experience

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
  "Research Assistant - University of Arkansas, Fayetteville, AR", "2019- 20", "", "Teach labs and perform research experiments.",
  "Assistant Manager - HotRose Pepper Sauce, Roseau, Dominica", "2018- 19", "", "Managing finances, marketing product, and running daily business.",
  "Summer Research Intern - Plant Pathology Department, University of Arkansas", "2018", "", "Operating Inverse Electron Microscope, analyzing and presenting research data, working in an interdisciplinary team including scientists from Physics and Plant Pathology.",
  "Lab Technician I - Plant Pathology Department, University of Arkansas", "2017-18", "", "Experimenting using multiple strains of bacteria and genera of 			rice plants, preparing LB, KB, and MS media for bacteria growth.",
  "Coffeehouse Committee Chair - University Programs, University of Arkansas", "2016-17", "", "Budgeting student activities fees, proposing student activities, leading team of 14 individuals, contacting agents and artists.",
  "Daytime Committee Chair - University Programs, University of Arkansas", "2015-16", "", "Budgeting student activities fees, proposing student activities, leading team of 14 individuals, contacting agents and artists.",
  "Data Entry Clerk/Administrative Assistant - National Employment Programme, Government of Dominica", "2014-15", "", "Drafting contracts, entering data, overseeing teaching interns, finding placements for interns, performing other administrative duties."
) %>% 
  detailed_entries(Degree, Year, Institution, Where)

```

# Activities & Honors

```{r}
tribble(
  ~Year, ~Type, ~Desc,
  "7-2019", "Scholarship Recipient", "NEON/TERENO Carbon Workshop",
  "06-19", "Scholar", "NEON-ESA Early Career Scholar",
  "05-2018", "Scholarship Recipient", "C. Roy Adair Plant Pathology Research Scholarship for Research",
  "05-2018", "Award Recipient", "University of Arkansas Graduating Student Leader",
  "02-2018", "Award Recipient", "Barbara Lofton Leadership Award",
  "2017 - 18", "Member", "Health and Occupation Safety Committee",
  "2017 - 18", "Vision Team Leader", "InterVarsity Christian Ministry",
  "2016 - 17", "Vice President", "Caribbean Student Association",
  "2016 - 17", "Small Group Leader", "InterVarsity Christian Ministry",
) %>% 
  brief_entries(
    glue::glue("{Type}"),
    Year, 
    Desc
  )
```

# Volunteer

* ESA Latin American Chapter, Co-Chair
* LifeSource After School Program
* Campus Food Pantry
* Yvonne Richardson Community Center