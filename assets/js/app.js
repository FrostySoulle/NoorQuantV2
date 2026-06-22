const hypotheses = [
{
title:"H0 - Universe Validity",
content:`
Can the current halal universe support a long-only intraday strategy?

Success:
Enough setups and liquidity exist.

Failure:
Too few opportunities.
`
},
{
title:"H1 - Relative Strength",
content:`
Stocks demonstrating stronger Relative Strength outperform weaker stocks.

Definitions:

RS_Open
RS_15
RS_30
RS_60
`
},
{
title:"H2 - Market Regime",
content:`
Trading performance differs across:

Bull Trend
Bear Trend
Sideways
`
},
{
title:"H3 - Breakout Continuation",
content:`
Opening Range Breakouts continue often enough to create positive expectancy.
`
},
{
title:"H4 - Volume Expansion",
content:`
Breakouts with elevated volume outperform breakouts without elevated volume.
`
},
{
title:"H5 - Absolute Strength Filter",
content:`
Price > Open
Price > VWAP

Improves performance compared to RS alone.
`
},
{
title:"H6 - Candidate Selection",
content:`
Top 3
Top 5
Top 10
Top 15

Determine optimal candidate pool.
`
}
];

const questions = [
"Q0 - Universe Validity",
"Q1 - Relative Strength",
"Q2 - Market Regime",
"Q3 - Opening Range Breakout",
"Q4 - Volume Expansion",
"Q5 - Absolute Strength Filter",
"Q6 - Candidate Selection",
"Q7 - Exit Strategy",
"Q8 - Costs & Slippage"
];

function createAccordion(containerId,data){

const container=document.getElementById(containerId);

data.forEach(item=>{

const accordion=document.createElement("div");
accordion.className="accordion";

accordion.innerHTML=`
<button class="accordion-header">
${item.title || item}
</button>

<div class="accordion-content">
${item.content || ""}
</div>
`;

container.appendChild(accordion);

});

}

createAccordion("hypotheses-container",hypotheses);
createAccordion("questions-container",questions);

document.addEventListener("click",e=>{

if(e.target.classList.contains("accordion-header")){

e.target.parentElement.classList.toggle("active");

}

});