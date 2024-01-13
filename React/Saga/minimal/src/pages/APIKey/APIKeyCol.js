import React from "react";

const Name = (cell) => {
  return cell.value ? cell.value : "";
};

const CreatedBy = (cell) => {
  return cell.value ? cell.value : "";
};

const APIKeys = (cell) => {
  return cell.value ? <span className="form-control">{cell.value}</span> : "";
};

const Status = (cell) => {
  return cell.value ? cell.value : "";
};
const CreatedDate = (cell) => {
  return cell.value ? cell.value : "";
};
const ExpiryDate = (cell) => {
  return cell.value ? cell.value : "";
};

export { Name, CreatedBy, APIKeys, Status, CreatedDate, ExpiryDate };
