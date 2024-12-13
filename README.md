### Simple Introduction for NICE Framework

We propose the <u>N</u>aive and <u>I</u>nsightful <u>C</u>ausal <u>E</u>valuation (NICE) framework. It accurately confirms the sign (positive or negative) of the causal effect and measures the reliability of causal effect evaluation results. The framework consists of two components: the Exclusive Naive Causal Effect Evaluation Model and the Tolerance Boundary Measurement Model. In the Exclusive Naive Causal Effect Evaluation Model, we begin by conducting an exclusivity assessment of the data. This step ensures that the causal analysis of the data is reduced to an analysis of its covariation, namely a correlation analysis. The coefficients obtained from this correlation analysis are then used to determine the sign of the causal effect. The second is the Tolerance Boundary Measurement Model, which assesses the trustworthiness of conclusions by leveraging the amount of data that supports the sign of the causal effect. This approach offers a precise measure of confidence in the evaluation results.

Judea Pearl proposes a representative method in the field of causal effect estimation [1].  It simulates randomized controlled experiments in the real world. By blocking the influence of backdoor paths in the causal graph, this method effectively reduces the interference of confounding factors, which is the foundation of the classical do-calculus theory [1]. However, as a traditional solution to causal effect estimation tasks, the correctness of the estimation results relies on the transition from $P\left(Y\middle| T\right)$, which describes correlation, to $P\left(Y\middle|\mathrm{do}\left(T\right)\right)$, which describes causation. Technically speaking, given $W$ contains the controlled variables, $Y$  denotes the outcome variable and $T$ represents the treatment (or cause) variable associtated with the causal effect, this transition can be calculated by $P\left(Y\middle|\mathrm{do}\left(T\right)\right)=\sum_{w\in W}P(w)P(Y|T,w)$. This formulation confines do-calculus to probabilistic models, limiting the exploration of its potential for broader applications.

Building on this insight, we propose a novel method for extending causal inference that transcends the limitations of probabilistic models. This approach enables new representations and analyses of multidimensional causal effects, such as stability and reliability. Specifically, by separating and characterizing the independent variable and confounding factors, we explicitly perform exclusivity analysis, thereby reducing causal analysis to correlation analysis. Leveraging a rich set of correlation analysis tools, this method adapts to non-traditional causal effect descriptions in complex causal scenarios, overcoming the expressive limitations of traditional probabilistic models.

Technically speaking, this method can be represented by

<img src="pic/README/fig1.svg" alt="fig1" align="middle">

where $Y$ denotes the outcome variable in the ordered binary causal relationship under investigation and $T$ represents the treatment (or cause) variable associtated with the causal effect. The vector $\mathbf{W}$ contains the controlled variables, forming the adjustment set that satisfies the backdoor criterion in [1] the causal graph, ensuring that confounding factors are properly accounted for. Finally, $U$ represents any unobserved exogenous variables that may influence the relationship. The functional relationship between the cause variable and the adjustment set variables should be decoupled in this functional expression. Considering the approximately linear relationships of causal variables in education [5], we present a development example of this method, namely the Exclusive Naive Causal Effect Evaluation Model. It is worth noting that the proposed NICE framework applies to educational contexts and holds potential for cross-disciplinary applications, such as treatment effect evaluation in medical data and policy effect analysis in economic models. It provides a plug-and-play correction for widely used statistical methods.

**The Exclusive Naive Causal Effect Evaluation Model.** The basic form of the model is set as follows:

<img src="pic/README/fig2.svg" alt="fig2" align="middle">

In addition to the variables inherited $(1)$, $\beta_0$ reflects the causal effect of exogenous variables on the outcome variable in the Structural Causal Model (SCM), while $\beta_1$ represents the causal effect of the cause variable $T$ on the outcome variable $Y$ after confounding adjustment. $\beta_2$ explains the additional influence of the controlled variables $\mathbf{W}$ on the outcome variable $Y$, and $\varepsilon$ is the error term, which includes errors caused by model assumptions incompleteness and other factors.

The causal analysis involves two key elements: covariation and exclusivity. While correlation analysis satisfies covariation, it cannot meet exclusivity due to confounding factors. Therefore, once the exclusivity assessment is completed, causal analysis of the data will be reverted to correlation analysis. Hence, the essence of this model is to control the set of variables $\mathbf{W}$ that satisfy the backdoor criterion to exclude the interference of confounding factors. Through the explicit exclusivity analysis via $\beta_2 \mathbf{W}$, the causal analysis is transformed into a discussion of correlation analysis. The direction of the causal effect between the ''cause'' and the ''effect'' is then determined by the sign of the coefficient $\beta_1$ from the correlation analysis between the ''cause'' and the ''effect''.

After determining the directionality of the causal effect, we further assess the reliability of the quantified causal effect. Existing causal effect evaluation methods focus primarily on the physical significance of the data but lack effective utilization of the data volume, which is crucial for determining the credibility of the conclusions. We address this gap in our approach. Specifically, when only a small amount of data supports a conclusion, its reliability is significantly compromised. In contrast, if extensive and widely applicable data support the conclusion, it suggests the identification of a more solid and reliable objective regularity. To address this, we propose the second component of the NICE framework, namely the Permissible Limits Measurement Model, to quantify the stability and reliability of the estimates derived from the naive causal effect evaluation model with exclusivity.

**The Tolerance Boundary Measurement Model.** In the context of the Exclusive Naive Causal Effect Evaluation Model, the permissible bounds for the resulting causal effect $\beta_1$ are defined as the $\mathrm{SE}\left(\beta_1\right)$ as follows:

<img src="pic/README/fig3.svg" alt="fig3" align="middle">

where $\mathrm{Var}\left(\beta_1\right)$ is the covariance matrix of the causal effect $\beta_1$​, defined as:

<img src="pic/README/fig4.svg" alt="fig4" align="middle">

Here, $X$ is an $n\times p$ design matrix that includes both the independent variables and control variables, where $n$ is the sample size, and $p$ is the number of model parameters; $y_i$ is the actual value of the $i-$th observation, $\widehat{y_i}$ is the predicted value for the $i-$th observation and $\sigma^2$ is the variance of the error term, which is estimated by the mean squared error of the sample residuals, denoted as ${\hat{\sigma}}^2$.

The tolerance boundary is defined as the square root of the variance to avoid non-intuitive fluctuations caused by huge dimensionality. The design matrix $X$ describes the relationships among the independent variables, including control variables. The use of $X^TX$ quantifies these correlations and their joint effect on causal effect estimation. Since the adjustment set for the backdoor path in a causal graph is typically correlated with the causal variables (connected through chain structures), we use the inverse matrix $\left(X^TX\right)^{-1}$ to avoid collinearity effects among the parameters, ensuring the independent contributions of each independent variable. By extracting $\left(X^TX\right)_{11}^{-1}$ and calculating its square root, we can assess the uncertainty associated with $\beta_1$.

### Simple Introduction for CI-PERO Framework

After ensuring a stable, positive causal relationship between the allocation of focal resources and the improvement of student educational outcomes, we consider the distribution of focal resources to achieve the maximum benefit of this educational investment for the student population as a whole. To this end, we propose the the 
<u>C</u>ausal <u>I</u>nference-based <u>P</u>recision <u>E</u>ducation <u>R</u>esource <u>O</u>ptimization (CI-PERO) framework and simplify it accordingly.

#### CI-PERO framework

After considering student psychology and school conditions, we classify students into four types based on their counterfactual behavior models after being incentivized: compliers, always-takers, never-takers, and defiers [2]. These classifications are presented as follows:

- Complier: If focal resources are not allocated to the school the student attends, the student will not use them to assist their learning. However, if focal resources are allocated to the school, the student will actively use them to support their learning;

- Always-taker: Whether focal resources are allocated to the student's school or not, the student will actively seek to use them to assist their learning;
- Never-taker: Whether focal resources are allocated to the student's school or not, the student will not use them to assist their learning;
- Defier: If focal resources are not allocated to the school the student attends, the student will independently explore using these resources to assist their learning. However, if focal resources are allocated to the school, the student will resist using them to support their learning.

Let the payoff for compliers be $\beta$, the payoff for always-takers be $\gamma$, the payoff for never-takers be $\theta$, and the payoff for defiers be $\delta$, resulting in the payoff vector $(\beta,\gamma,\theta,\delta)$. Our objective is to identify a characteristic $c$ of a particular student population that maximizes the value of the following equation [3,4]:

<img src="pic/README/fig5.svg" alt="fig5" align="middle">

Since the behavior pattern of compliers best reflects the effect of resource allocation measures, we aim to select the student group with the highest proportion of compliers, thereby maximizing the benefit of resource allocation in improving educational quality.

Let $P=p$ indicate the allocation of focal resources, and $P=p^{'}$ represent the opposite. Let $U=u$ suggest that the student actively uses the focal resources and $U=u^{'}$ suggest the opposite. In this way, $u_p$ represents the case where the student actively uses the resource when focal resources are allocated; $u_{p^{'}}$ represents the case where the student actively uses the resource when no focal resources are allocated; $u_p^\prime$ represents the case where the student passively uses the resource when focal resources are allocated; and $u_{p^{'}}^{'}$ represents the case where the student passively uses the resource when no focal resources are allocated. Thus, the CI-PERO framework defines the objective function as the average benefit obtained from each student after allocating focal resources to the student group with characteristic $c$. Therefore, \eqref{equ:all_benefit_function} can be rewritten as:

<img src="pic/README/fig6.svg" alt="fig6" align="middle">

At this point, we have presented the general form of the CI-PERO framework. However, these four types of individuals do not always coexist in practical scenarios. When a certain kind of individual is absent, the calculation of $f(\beta, \gamma, \theta, \delta)$ will be significantly simplified.

### Key File Introduction

Causal Discovery/cmd.txt 我们使用Tetrad进行因果发现，这是我们的参数设置情况，在此基础上我们辅以专家领域知识对边进行修改

Mutual information causal screening/DataProcessMI-and-CalMI.ipynb 我们使用互信息完成PISA 2022中所有指标与学生成绩的因果筛查

Experimental verification of NICE synthetic dataset/exp.ipynb 我们自行创建了模拟数据集，并在这个数据集上验证了我们的NICE框架





### Reference

[1] Judea Pearl and Dana Mackenzie. The book of why: the new science of cause and effect. Basic books, 2018.

[2] Joshua D Angrist, Guido W Imbens, and Donald B Rubin. Identification of causal effects using instrumental variables. Journal of the American statistical Association, 91(434):444–455, 1996

[3] Ang Li and Judea Pearl. Unit selection based on counterfactual logic. In Proceedings of the Twenty-Eighth International Joint Conference on Artificial Intelligence, 2019.

[4] Ang Li and Judea Pearl. Unit selection with causal diagram. In Proceedings of the AAAI conference on artificial intelligence, volume 36, pages 5765–5772, 2022.

[5] Minseok Yang and Ho Jun Lee. Do school resources reduce socioeconomic achievement gap? evidence from pisa 2015. International Journal of Educational Development, 88:102528, 2022

