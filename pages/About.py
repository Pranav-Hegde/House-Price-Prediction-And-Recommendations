
import streamlit as st

st.header("About This App")

st.markdown("""
**House Recommendation and Prediction App**  
This application helps users discover suitable properties and predict house prices using advanced machine learning techniques.

---

### 🧠 Algorithm Used: Random Forest Regressor

- **Random Forest Regression** is an ensemble learning algorithm that builds multiple decision trees and combines their outputs for more accurate and robust predictions.
- Each tree in the forest is trained on a random subset of the data and considers a random subset of features at each split. This randomness helps to reduce overfitting and increases the model’s generalization ability[1][3][5].
- For regression tasks (like house price prediction), the final prediction is the average of all the individual trees’ predictions[3][4].
- Random Forest is widely used due to its flexibility, ability to handle missing values, and high performance on complex datasets[5].

---

### 🔬 Why Random Forest?

- **Accuracy:** By averaging the predictions of many trees, Random Forest typically achieves higher accuracy than a single decision tree.
- **Robustness:** It is less likely to overfit, making it reliable for real-world predictions.
- **Interpretability:** Feature importance scores from the model help users understand which factors most influence price predictions.

---

### 📚 References

- [Wikipedia: Random Forest][3]
- [scikit-learn documentation][4]
- [IBM: What Is Random Forest?][5]

---

*Built with ❤️ using Streamlit and scikit-learn.*
""")
