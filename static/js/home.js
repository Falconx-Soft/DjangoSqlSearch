const pillarOption = document.querySelectorAll("#pillarOption");
const sourceTypeOption = document.querySelectorAll("#sourceTypeOption");
const marketOption = document.querySelectorAll("#marketOption");
const brandSourceOption = document.querySelectorAll("#brandSourceOption");


let pillarSelection = "";
let sourceTypeSelection = "";
let marketSelection = "";
let brandSourceSelection = "";


for(let i=0; i<pillarOption.length; i++){
	pillarOption[i].addEventListener("click", function(){
		pillarSelection = "pillar = \""+pillarOption[i].innerHTML+"\"";
		document.getElementById("pillarBtn").innerHTML = pillarOption[i].innerHTML +" <i class='feather icon-chevron-down'></i>";
	});
}

for(let i=0; i<sourceTypeOption.length; i++){
	sourceTypeOption[i].addEventListener("click", function(){
		sourceTypeSelection = "sourceType = \""+sourceTypeOption[i].innerHTML+"\"";
		document.getElementById("sourceTypeBtn").innerHTML = sourceTypeOption[i].innerHTML +" <i class='feather icon-chevron-down'></i>";
	});
}

for(let i=0; i<marketOption.length; i++){
	marketOption[i].addEventListener("click", function(){
		marketSelection = "market = \""+marketOption[i].innerHTML+"\"";
		document.getElementById("marketBtn").innerHTML = marketOption[i].innerHTML +" <i class='feather icon-chevron-down'></i>";
	});
}

for(let i=0; i<brandSourceOption.length; i++){
	brandSourceOption[i].addEventListener("click", function(){
		brandSourceSelection = "brandSource = \""+brandSourceOption[i].innerHTML+"\"";
		document.getElementById("brandSourceBtn").innerHTML = brandSourceOption[i].innerHTML +" <i class='feather icon-chevron-down'></i>";
	});
}

document.getElementById("searchByFilterBtn").addEventListener("click", function(){
	const searchByFilterQuery = document.getElementById("searchByFilterQuery");
	let queryString = "SELECT * From searchapp_reviews WHERE ";
	let firstEntry = true;
	if (pillarSelection != ""){
		queryString = queryString + pillarSelection;
		firstEntry = false;
	}

	if (sourceTypeSelection != ""){
		if(firstEntry == true){
			queryString = queryString + pillarSelection;
			firstEntry = false;
		}else{
			queryString = queryString +" And "+pillarSelection;
		}
		
	}

	if (marketSelection != ""){
		if(firstEntry == true){
			queryString = queryString + marketSelection;
			firstEntry = false;
		}else{
			queryString = queryString +" And "+marketSelection;
		}
	}

	if (brandSourceSelection != ""){
		if(firstEntry == true){
			queryString = queryString + brandSourceSelection;
			firstEntry = false;
		}else{
			queryString = queryString +" And "+brandSourceSelection;
		}
	}

	const startDate = document.getElementById("startDate");

	const endDate = document.getElementById("endDate");

	if(startDate.value != "" && endDate.value != ""){

		// console.log(startDate.value)
		// startDateTemp = startDate.value.split("-");
		// console.log(startDateTemp)
		// newStartDate = startDateTemp[2]+"-"+startDateTemp[1]+"-"+startDateTemp[0]
		// console.log(newStartDate)

		// endDateTemp = endDate.value.split("-");
		// newEndDate = endDateTemp[2]+"-"+endDateTemp[1]+"-"+endDateTemp[0]

		if(firstEntry == true){
			queryString = queryString +"created_at BETWEEN \""+startDate.value+"\" AND \""+endDate.value+"\"";
			firstEntry = false;
			console.log(queryString);
		}else{
			queryString = queryString +"AND created_at BETWEEN \""+startDate.value+"\" AND \""+endDate.value+"\"";
			console.log(queryString);
		}
	}

	searchByFilterQuery.value = queryString;
	document.getElementById("searchByFilterQuerySubmit").click();
})