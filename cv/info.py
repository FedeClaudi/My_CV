from myterial import green_light

highlight = f"bold italic {green_light}"


BIO = {
    "name": "Federico Claudi",
    "email": "federico.claudi.17@ucl.ac.uk",
    "website": "https://fedeclaudi.github.io",
    "github": "https://github.com/FedeClaudi",
    "twitter": "https://twitter.com/Federico_claudi",
}

open_source_projs = {
    "brainglobe": [
        "The brainglobe atlas API (BG-AtlasAPI) provides a common interface for programmers to download and process brain atlas data from multiple sources.",
        "brainglobe/bg-atlasapi",
        "https://docs.brainglobe.info/bg-atlasapi/usage",
    ],
    "brainrender": [
        "brainrender is a python package for the visualization of three dimensional neuro-anatomical data. The goal of brainrender is to facilitate the exploration and dissemination of neuro-anatomical data.",
        "brainglobe/brainrender",
        "https://docs.brainrender.info/",
    ],
    "pyinspect": [
        "pyinspect, the python package for lazy programmers. Inspect your code, improve tracebacks and automatic googling for bug fixes.",
        "FedeClaudi/pyinspect",
        "https://github.com/FedeClaudi/pyinspect",
    ],
    "refy": [
        "A better literature recomendation system.",
        "FedeClaudi/refy",
        "https://github.com/FedeClaudi/refy",
    ],
}

education = {
    (2017, "now "): [
        f'PhD in [{highlight}]"Experimental and theoretical systems neuroscience"[/{highlight}]',
        "Dr. Tiago Branco",
        "Sainsbury Wellcome Centre [dim]UCL",
    ],
    (2015, 2016): [
        f'Master in Research in [{highlight}]"Integrative Neuroscience"[/{highlight}]',
        "Dr. Ian Duguid",
        "University of Edinburgh",
    ],
    (2012, 2015): [
        f'Bachelor in [{highlight}]"Medical Biotechnologies"[/{highlight}]',
        "Dr. Ian Duguid",
        "University of Edinburgh",
    ],
}

research_experience = {
    (2017, "now "): [
        "PhD research project [dim](4 years)",
        "Sainsbury Wellcome Centre,[dim] UK",
        "Dr. Tiago Branco.",
    ],
    (2016, 2017): [
        "Visiting scientist [dim](1 year)",
        "University of Edinburgh,[dim] UK",
        "Dr. Ian Duguid.",
    ],
    (2015, 2016): [
        "Master project [dim](1 year)",
        "University of Edinburgh,[dim] UK",
        "Dr. Ian Duguid.",
    ],
    (2015, 2015): [
        "Bachelor dissertation project [dim](4 months)",
        "Katholiege Universitei,[dim] Leuven, Belgium",
        "",
    ],
    (2011, 2011): [
        "Summer internship [dim](1 month)",
        "Columbia university,[dim] New York City, USA",
        "Dr. Filippo Mancia",
    ],
    (2011, 2011): [
        "Summer internship [dim](1 month)",
        "Università degli Studi,[dim] Milano, Italy",
        "",
    ],
    (2010, 2010): [
        "Summer internship [dim](1 month)",
        "Columbia university,[dim] New York City, USA",
        "Dr. Filippo Mancia",
    ],
}

extracurr_education = {
    ("2015a"): [
        f'Online Course in [{highlight}]"Medical Neuroscience"',
        "Duke University, USA",
        "Attended on: coursera.org",
    ],
    ("2015b"): [
        f'Online Course in [{highlight}]"Synapses, Neurons and Brain"',
        "Hebrew University, Jerusalem, Israel",
        "Attended on: coursera.org",
    ],
}

teaching_experience = {
    (20202019): [
        f"[link=https://www.xhmfoundation.com/braincamp-kosovo-2020s]Teacher at [{highlight}]Braincamp",
        "XhM Foundation",
    ],
    (2020): [
        f"Teaching Assistant at [{highlight}]NeuroMatchAcademy.",
        "Neuromatch Academy",
    ],
    (2019): [
        f"[link=https://www.xhmfoundation.com/braincamp-kosovo-2019]Teacher at [{highlight}]Braincamp",
        "XhM Foundation",
    ],
    (2016): [
        "Training of colleagues in microsurgical and behavioural techniques",
        "University of Edinburgh,[dim] Edinburgh",
    ],
}

publications = {
    (1, 2021): [
        "Visualizing anatomically registered data with brainrender.",
        "[bold green]F Claudi[/bold green], AL Tyson, L Petrucco, TW Margrie, R Portugues, T Branco",
        "[italic]eLife",
        "[link=https://elifesciences.org/articles/65751]doi.org/10.7554/eLife.65751",
    ],
    (2, 2021): [
        "Tools for accurate post hoc determination of marker location within whole-brain microscopy images.",
        "Adam L Tyson, Mateo Vélez-Fort, Charly V Rousseau, Lee Cossell, Chryssanthi Tsitoura, Horst A Obenhaus, [bold green]Federico Claudi[/bold green], Stephen C Lenzi, Tiago Branco, Troy W Margrie",
        "[italic]bioRxiv",
        "[link=https://www.biorxiv.org/content/10.1101/2021.05.21.445133v1.abstract]doi.org/10.1101/2021.05.21.445133 ",
    ],
    (3, 2020): [
        "BrainGlobe Atlas API: a common interface for neuroanatomical atlases.",
        "[bold green]Federico Claudi[/bold green], Luigi Petrucco, Adam L. Tyson, TiagoBranco, Troy W. Margrie, and Ruben Portugues",
        "Journal of Open Source Software",
        "[link=https://doi.org/10.21105/joss.02668]doi.org/10.21105/joss.02668",
    ],
    (4, 2020): [
        "Brainrender. A python based software for visualisation of neuroanatomical and morphological data\n",
        "[bold green]Federico Claudi[/bold green], Adam L. Tyson, Tiago Branco",
        "[italic]bioRxiv (2020)",
        "[link=https://doi.org/10.1101/2020.02.23.96174]doi.org/10.1101/2020.02.23.96174",
    ],
    (5, 2019): [
        "Cerebellar-recipient motor thalamus drives behavioral context-specific movement initiation",
        "Joshua Dacre, Matt Colligan, Julian Ammer, Julia Schiemann, Thomas Clarke, Victor Chamosa-"
        + "Pino, [bold green]Federico Claudi[/bold green], J. Alex Harston, Constantinos Eleftheriou, Janelle M.P. Pakan, Cheng-Chiu"
        + "Huang, Adam Hantman, Nathalie L. Rochefort, Ian Duguid",
        "[italic]bioRxiv (2019)",
        "[link=https://doi.org/10.1101/80212]doi.org/10.1101/802124",
    ],
    (6, 2016): [
        "CXCL4 and CXCL4L1 Differentially Affect Monocyte Survival and Dendritic Cell Differentiation and Phagocytosis.",
        "Gouwy M, Ruytinx P, Radice E, [bold green]Claudi F[/bold green], Van Raemdonck K, Bonecchi R",
        "[italic]PLoS ONE (2016)",
        "[link=https://doi.org/10.1371/journal.pone.016600]doi.org/10.1371/journal.pone.0166006",
    ],
}

posters = {
    (2020): [
        "Fast unsupervised learning and innate heuristics support escape path selection",
        "[bold green]Federico Claudi[/bold green], Dario Campagner, Tiago Branco",
        "Bernstein Conference",
    ]
}


awards = {
    (2020): [
        "Wellcome Trust 4-Year PhD Fellowship.",
        "Sainsbury Wellcome Centre,[dim] University College London",
    ],
    (2015): [
        "Erasmus scholarship for the bachelor project in Leuven, Belgium. ",
        "Università degli Studi,[dim] Milano, Italy",
    ],
}
