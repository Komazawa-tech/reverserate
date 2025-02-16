document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.getElementById("toggle-advanced-search");
    const advancedFields = document.getElementById("advanced-search-fields");
  
    // 詳細検索フィールドのトグル用フラグ
    let isAdvancedVisible = false;
  
    // ボタンクリックで表示/非表示を切り替える
    toggleButton.addEventListener("click", function() {
      if (!isAdvancedVisible) {
        advancedFields.style.display = "block";
        toggleButton.textContent = "詳細検索フィールドを非表示";
      } else {
        advancedFields.style.display = "none";
        toggleButton.textContent = "詳細検索フィールドを表示";
      }
      isAdvancedVisible = !isAdvancedVisible;
    });
  });
  