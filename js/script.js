let selectedOp = "+";

const dropdown = document.getElementById("opSelect");
const selectedIcon = document.getElementById("selectedIcon");
const items = document.querySelectorAll(".dropdown-item");

// Toggle dropdown
dropdown.onclick = function(e) {
    e.stopPropagation();
    dropdown.classList.toggle("active");
};

// Select operation
items.forEach(item => {
    item.onclick = function(e) {
        e.stopPropagation();
        selectedOp = item.getAttribute("data-op");
        selectedIcon.textContent = item.textContent;
        dropdown.classList.remove("active");
    };
});

// Close dropdown if clicking outside
document.addEventListener("click", function() {
    dropdown.classList.remove("active");
});

// Calculate button
document.getElementById("calcBtn").onclick = function() {
    let a = parseFloat(document.getElementById("numA").value);
    let b = parseFloat(document.getElementById("numB").value);

    if (isNaN(a) || isNaN(b)) {
        document.getElementById("result").innerText = "Result: Invalid input!";
        return;
    }

    let result;

    switch (selectedOp) {
        case "+": result = a + b; break;
        case "-": result = a - b; break;
        case "*": result = a * b; break;
        case "/":
            if (b === 0) {
                document.getElementById("result").innerText = "Result: Division by zero!";
                return;
            }
            result = a / b;
            break;
    }

    document.getElementById("result").innerText = "Result: " + result;
};
