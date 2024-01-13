import React from "react";

const Name = (cell) => {
  return cell.value ? cell.value : "";
};

const CreatedBy = (cell) => {
  return cell.value ? cell.value : "";
};

const APIKeys = (cell) => {
  return (
    <input type="text" className="form-control apikey-value" readOnly defaultValue={cell.value} />
  )
};

const Status = (cell) => {
  return (
    <span className={`${cell.value === 'Disable' ? "badge bg-danger-subtle text-danger" : "badge bg-success-subtle text-success"}`}>{cell.value ? cell.value : ""}</span>
  );
};
const CreatedDate = (cell) => {
  return cell.value ? cell.value : "";
};
const ExpiryDate = (cell) => {
  return cell.value ? cell.value : "";
};

export { Name, CreatedBy, APIKeys, Status, CreatedDate, ExpiryDate };
