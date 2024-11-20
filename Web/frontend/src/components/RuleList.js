import React, { useEffect, useState } from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";
import RuleForm from "./RuleForm";
import "./css/RuleList.css";

function RuleList() {
  const [rules, setRules] = useState([]);
  const [editingRule, setEditingRule] = useState(null);

  // Fetch rules from the backend
  useEffect(() => {
    axios
      .get("http://localhost:5000/api/rules")
      .then((response) => setRules(response.data))
      .catch(() => {});
      // .catch(() => toast.error("Error fetching rules"));
  }, [rules]);

  // Delete a rule with confirmation
  const deleteRule = (id) => {
    if (window.confirm("Are you sure you want to delete this rule?")) {
      axios
        .delete(`http://localhost:5000/api/rules/${id}`)
        .then(() => {
          toast.success("Rule deleted successfully");
        })
        .catch(() => {
          toast.error("Error deleting rule");
        });
    }
  };

  // Set the rule to be edited
  const editRule = (rule) => {
    setEditingRule(rule);
  };

  return (
    <div>
      <h2>Firewall Rules</h2>
      <RuleForm
        editingRule={editingRule}
        setEditingRule={setEditingRule}
        setMessage={toast}
      />
      <div className="rules-list">
        {rules.length === 0 && <p>No rules available</p>}
        {rules.map((rule) => (
          <div key={rule.id} className="card">
            <div className="card-header">{`Rule #${rule.id}`}</div>
            <div className="card-content">
              <p>
                <strong>Source IP:</strong> {rule.source_ip}
              </p>
              <p>
                <strong>Destination IP:</strong> {rule.destination_ip}
              </p>
              <p>
                <strong>Source Port:</strong> {rule.source_port}
              </p>
              <p>
                <strong>Destination Port:</strong> {rule.destination_port}
              </p>
              <p>
                <strong>Protocol:</strong> {rule.protocol}
              </p>
              <p>
                <strong>Action:</strong> {rule.action}
              </p>
            </div>
            <div className="card-actions">
              <button onClick={() => editRule(rule)}>Edit</button>
              <button onClick={() => deleteRule(rule.id)}>Delete</button>
            </div>
          </div>
        ))}
      </div>
      <ToastContainer
        position="bottom-right" // Sets toast position to bottom-right
        autoClose={5000} // Optional: Auto close after 3 seconds
        hideProgressBar={false} // Optional: Show or hide progress bar
        newestOnTop={true} // Optional: Show newest toast at the top
        closeOnClick // Optional: Close toast on click
        pauseOnHover // Optional: Pause toast when hovered
        draggable // Optional: Allow dragging the toast
      />
    </div>
  );
}

export default RuleList;
