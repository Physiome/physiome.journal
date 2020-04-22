Title: Instructions to Authors
Slug: instructions-to-authors

Instructions to Authors
-----------------------
The main task for a *Physiome* paper is to provide a citable link between a published, validated model and its instance in the [Physiome Model Repository (PMR)](https://models.physiomeproject.org) or corresponding repository or database. The model files submitted must fulfill the demands of reusibility stated by the [Physiome Project](https://physiomeproject.org). All submissions to *Physiome* must also be associated with one, or more, articles accepted by peer-reviewed physiology, bioengineering or biophysics journals, here refered to as a *primary publication*. Authors are encouraged to prepare their Physiome submission(s) in parallel to the primary paper. Submissions will not be curated and evaluated until the primary paper is accepted, but authors will be able to access and share their submission via the PMR. Please contact *Physiome* (physiome@physiomeproject.org) if you have any queries. 


### 1. Preparing your submission
Submissions should be prepared using the Overleaf template (LINK) or MS Word template (LINK). These templates will provide the main document for the submission, but the submission must include all resources required to evaluate the reproducibility, reusability, and discoverability of the submission. As described in the templates, such resources can be directly included in the Overleaf project or zip archive, or linked to via appropriate online repositories or databases.

* **1.1 Information included in your *Physiome* paper **

A *Physiome* paper is a description of the model submitted to the repository. If the model code submitted is complete, all parameter values, units, etc will be included in the files and do not to be printed in the article. 
The paper should include: i) reference(s) to  the primary paper(s); ii) figures showing that the code simulates the same graphs as shown in the primary paper; iii) any modifications made to the model, including motivations and origin; iv) references to the origins of the parameter values, if other than the primary paper; v) a brief explanation of the biological system modelled. 

It is encouraged that the authors of the primary primary paper are included in the *Physiome* paper. The *Physiome* team can help with reaching out to them if needed. 


* **1.2 SOME INSTRUCTIONS ABOUT FIGURES AND MODEL FILES. I GUESS THESE DEPENDS ON THE SUBMISSION SYSTEM.**


### 2. Types of submissions
The following types of submissions will be considered for publication in *Physiome*.  [Here you can find templates and examples for the different types of submissions.](articles)  (LINK)

* **2.1 Original submission**

	Original submissions are author initiated submissions directly associated with a primary experimental or modelling paper that has been accepted by a peer-reviewed physiology, bioengineering, or biophysics journal. While matching authorship between the Physiome submission and the primary article is not a requirement, it is expected that there is at least some overlap for original submissions. The purpose of a Physiome paper is to provide a citable framework that tie the model files stored in the Physiome Model Repository to its primary publication. Therefore, a Pysiome original paper is structured a bit differently than most papers published in scientific journals and some sections normally expected to be in a scientific paper are not required in a Physiome paper. Below is listed the minimal information required in an original Physiome paper. As we recognize that different models and different primary papers require different information, feel free to add any sections that are necessary to give a clear description of the model. However, keep in mind that most of the information necessary to run the model, such as parameter values and units, are already present in the model files and does not need to be repeated in the paper itself.  

* **2.2 Retrospectives**

	A retrospective is similar in most regards to an original submission, but is associated with an historical primary article which has been deemed to provide substantial value to the physiological modelling community in making a reusable, reproducible, and discoverable version of the study available. Where possible, the authors of retrospective submissions should include authors from the primary article. Retrospectives may be invited by the *Physiome* editors or can be author initiated. When submitting a retrospective, it is best to first submit an expression of interest to the editors outlining why the original primary paper should be considered a suitable contribution to *Physiome*.

* **2.3 Reviews**

	The *Physiome* editorial board may solicit review submissions that document a range of published models in a given area. Such reviews will make use of previously accepted *Physiome* submissions, often applying new data or simulation experiments to explore the capabilities of the various models.

* **2.4 Letters**

	A letter is an original submission that provides new insights about, or refinement of, a model that is already published on the Physiome site. This format allows publication of material that in itself may not justify a separate submission to a primary peer-reviewed journal, but which may still be highly instrumental for improving an existing model, expand its empirical scope or invoke experimental and theoretical research that may drive new model development. Examples of such material include, but are not restricted to, experimental measurements of important parameter values that have been only indirectly estimated in the original paper, empirically or theoretically justified questioning or refutation of critical model premises, experimental data confirming or refuting model predictions, and theoretical analyses of the model that provide novel insights that may spur further model development or experimental work.
    
   
	
    ### 3. Model Code Submission

    
    **3.1 Where can I submit my code?**
    
    The model files submitted must fulfill the demands of reusibility stated by the [Physiome Project](https://physiomeproject.org). *Physiome* accepts code submitted to any repository shown to be open access, permanent and version controlled. 
    
    The Physiome Project has an associated repository for this purpose, the Physiome Model Repository (PMR) (LINK), which we encourage authors to use. Upon receipt of a submission which is not already linked to a repository, curators will create a private PMR workspace for the submission – a version controlled repository within PMR. When a Physiome submission consists of models or data already in PMR, then that will be linked to this submission workspace internally to PMR. 
    
    The figure below presents an overview of the flow of a Physiome submission from the point at which it is submitted through preliminary checking, curation and evaluation, and the final deposition in the Physiome Figshare portal upon a successful evaluation. We describe below this sequence in detail.
    
    <div style = "text-align: center;">
    
    <img src="/assets/CurationAndSubmissionFlow.png" alt="Curation flow" style="width:70%;height:70%;">
    
    </div>

    The Physiome editors will first check that a submission meets the minimum requirements for evaluating reproducibility. These requirements are listed below.
    
    <body>
    <dl type="1">
    <dt>1.    There is a clear link to:
    <dd>a.    primary paper for original and retrospective submissions;
    <dd>b.    existing Physiome article for a letter; or
   <dd> c.    both for reviews.
     <dt>2.    The submission relates to one or more quantitative models.
     <dt>3.    Reproducible targets clearly identified.
    <dd>a.    Must include at least some predictions from the primary paper.
    <dd>b.    May include further validation, testing, estimation, etc., targets not directly reported in primary paper.
    <dt>4.    Model implementation(s) is executable.
    <dd>a.    The curation team must be able to execute the simulations required to test the reproducibility of the model(s).
   <dd> b.    These may require specific software tools, but details for non-standard tools must be provided.
   <dl>
   <body>
   
    If a submission meets these minimum requirements the submission will proceed to curation.
    
    For maximal reusability, reproducibility, and discoverability, it is essential for mathematical models and simulation experiments to be encoded in appropriate standard formats. The IUPS Physiome Project follows the guidance of the [Computational Modelling in Biology Network (COMBINE)](https://co.mbine.org) as to which standards are appropriate for various types of data.
    The scope of computational models expected to be submitted to Physiome will often exceed what the current standard formats are able to represent, but a key role of the curators is to identify models, or parts of models, which should be encoded in a standard format. When such an identification is made, the curators will work with the authors to try and encode the model in that format.
    It is important to note that while the appropriate use of standard formats will inform the evaluation of a Physiome submission, capabilities of current accepted standards and software tools should not impede the submission of a piece of work to Physiome. It is, however, the remit of Physiome to inform the standards communities as to requirements for eventually can represent all models and simulation experiments accepted to Physiome.

    **3.2 What files do I need to submit?**
All files needed to run and simulate the model, including plotting the figures. Also include a Read Me file.
        
    * **3.3 Curation**
    
    Once submitted to the PMR, the model will be curated, ensuring that it can simulate the figures of the primary paper, as persented in the Physiome submission. 
    A full CellML model submission must include: 
    
    <body>
    <ul>
    <li>Annotation 
    <li> Units
    <li> All parameter values and initial values
    <li> All equations
    <li> Possibility to plot all variables
    <ul>
    <body>
    
    <div>
    
    If you submit a model in any other format than CellML, you need to submit a document specifying where to find the corresponding information. 
    
    Curators will extract the reproducibility targets from the original submission and annotate the submission’s PMR workspace with the information required to completely describe the targets. This will include the specific simulation experiments that need to be performed and the data to be extracted from the target and simulation results to provide a quantitative measure of comparison.
    The curators will then execute the required simulation experiments and perform the comparison to determine a measure of reproducibility. 
    
    The following criteria will be considered when evaluating reproducibility.
    
    <body>
    <dl type="1">
    <dt> 1.    Are the required simulation experiments available?
    <dd> -    Require only standard tools or access to tools is provided.
    <dd> -    Or standard formats used.
    <dt> 2.    Can the simulation experiments be executed?
    <dt> 3.    Do the model predictions match the targets?
    <dt> 4.    Repeatable vs reproducible
    <dd> -    Matlab code that only works in Matlab is repeatable but not reproducible
    <dd> -    Code that only works with a given library may be repeatable but not reproducible.
    <dd> -    Standard formats used for everything, simulation experiments can be performed in a different tool to that used in the primary paper => reproducible?
    <dt> 5.    Coverage? Testing?
    <dl>
        <body>
    
    Evaluating reusability: Same as above, but now dealing with how understandable/comprehensible the submission is.
    
    <body>
    <ol type="1">
    <li>    Parameter sources clearly identified
   <li>     Provenance is clear
    <li>    Algorithms used specified, and their parameterisations
    <li>    Appropriate standards used
    <li>    Modularity
    <li>    Availability of code and its accessibility (undocumented spaghetti code vs well documented structured code)
    <li>    Annotation
    <ol>
    <body>
    
    
### 4. Primary Publication
    
* **4.1 What is a Primary Publication and why do I need one?**
    
The primary publication is an experimental/modelling paper that has been accepted to a peer-reviewed physiology, bioengineering or biophysics journal. The primary paper shows that the model is validated by describing the experiments and data, and the model(s) fit to the data, as well as the biological background and why the model is important. Physiome papers will describe the details of mathematical models and computational simulations associated with a ‘primary’ has been accepted by a recognised peer-reviewed journal, but does not deal with the validation of the models. Therefore, every Physiome paper needs to be associated with a primary paper. 

### 5. Cost
    
Physiome papers are citable with a DOI and published as open access with an author processing charge of US$300. The fee is to be paid after acceptance of the submission, but before publication. See payment terms. (LINK)
    
### 6. Copyright of submission


