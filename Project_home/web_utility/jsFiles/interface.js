function request_major(){
	var major = document.getElementById("major_name").value;
	
	return major

}
function request_classes(){
	var class_taken=document.getElementsByClassName("classTaken");
	var all_rating=document.querySelectorAll("input[type=radio]");
	var class_rating= new Array();
	for(i=0;i<all_rating.length;i++){
		if(all_rating[i].checked){
			class_rating.push(all_rating[i].value);
		}
	
	}
	
	return class_taken

}
function add_class_selection(){
	var list=document.getElementById("class_list");
	var input=document.createElement("INPUT");
	input.type = "text";
	input.setAttribute("class","classTaken");
	var ul=document.createElement("UL");
	var li1 = document.createElement("LI");
	var li2 = document.createElement("LI");
	var li3 = document.createElement("LI");

	var li1Input = document.createElement("INPUT");
	var li2Input = document.createElement("INPUT");
	var li3Input = document.createElement("INPUT");
	
	var div = document.createElement("DIV");
	div.setAttribute("class","classDiv");
	div.setAttribute("id","classId");

	var pText = document.createElement("P");
	pText.innerHTML="How would you rate this class";

	li1Input.type="radio";
	li1Input.value="1";
	li1.innerHTML="1";
	li2Input.type="radio";
	li2Input.value="2";
	li2.innerHTML="2";
	li3Input.type="radio";
	li3Input.value="3";
	li3.innerHTML="3";
	li1.appendChild(li1Input);
	li2.appendChild(li2Input);
	li3.appendChild(li3Input);
	ul.appendChild(li1);
	ul.appendChild(li2);
	ul.appendChild(li3);
	
	div.appendChild(input);
	div.appendChild(pText);
	div.appendChild(ul);
	list.appendChild(div);
	
}
