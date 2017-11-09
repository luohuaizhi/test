namespace cpp fetch_thirdparty
namespace java fetch_thirdparty

struct BindThirdpartyRequest {
  1: string uid,
  2: string access_token,
  3: i32 bind_type,
  4: i64 user_id,
}

struct SendCaptchaRequest {
  1: string captcha,
  2: i64 user_id,
}

struct RebindChsiResponse {
  1: i32 retcode,     #0:直接拉取成功，无需后续操作. -1:需要填验证码. -2:其他原因导致拉取失败
  2: optional string captcha,
  3: optional string errmsg,
}

struct BindChsiRequest {
  1: string username,
  2: optional string password,
  3: i64 user_id,
  4: i32 type,
  5: optional string captcha,
}

struct BindChsiResponse {
  1: i32 retcode,
  2: optional string errmsg,
  3: optional string captcha,
}

struct QueryLoanRequest {
  
}

#以下是yunsign增加的数据结构
struct RepayInfo {
  1: string desc,         #例如：第一期、第二期
  2: i32 amount,          #当期还款金额
  3: string repay_date,   #预计还款日期，例如2015-01-01
}

struct ServerCreateContractRequest{
  1: i64 uin,
  2: optional string phone,
  3: optional string name,
  4: optional string id_card_number,
  5: i64 amount,
  6: i32 interest,
  7: string interest_rate,
  8: i32 service_fee,
  9: string service_fee_rate,
  10: string apply_days,
  11: i32 interest_day,
  12: string bank_list,
  13: string bank_number,
  14: i32 before_day,
  15: string overdue,
  16: string apply_date,
  17: list<RepayInfo> repay_list,
  18: string contract_temp_number,
}

struct ServerCreateContract2Request{
  1: i64 uin,
  2: optional string phone,
  3: optional string name,
  4: optional string id_card_number,
  5: i64 amount,
  6: i32 interest,
  7: string interest_rate,
  8: i32 service_fee,
  9: string service_fee_rate,
  10: string apply_days,
  11: string bank_list,
  12: string bank_number,
  13: string overdue,
  14: string apply_date,
  15: list<RepayInfo> repay_list,
  16: string back_bank_list,
  17: string back_bank_number,
  18: string contract_temp_number,
  19: i32 interest_day,
  20: string bank_branch_name,
  21: i32 stage_type,
  22: string month_manage_fee,
  23: string month_interest,
  24: i64 pre_safe_amount,
}

struct ContractResponse{
  1: i32 ret_code,
  2: string last_contract_id,
  3: string contract_url,
}

struct SendMsgRequest{
  1: i64 uin,
  2: string last_contract_id,
  3: string phone,
}

struct ContactShowRequest{
  1: i64 uin,
  2: string contract_id,
  3: string phone_no,
}

struct ContractStatusRequest{
  1: i64 uin,
  2: string contract_id,
  3: string phone_no,
}

struct SignRequest{
  1: i64 uin,
  2: string last_contract_id,
  3: string code,
}

struct DownloadRequest{
  1: i64 uin,
  2: string last_contract_id,
}

struct SignResponse{
  1: i32 result_code,
  2: string error_msg,
}

struct SendMsgResponse{
  1: i32 ret_code,
  2: string msg,
}

struct GetContractResponse{
  1: string url,
  2: i32 status,
}

struct CheckBlackListRequest {
  1: i64 user_id,
  2: string feature_list,
}

struct SmallPayRequest{
  1: i64 apply_id,
  2: i64 user_id,
  3: string bank_code,
  4: string bank_no,
  5: string user_name,
  6: string user_id_no,
  7: string user_phone_no,
  8: string bussiness_amount,
}

struct SmallPayResponse {
  1: string sign_value,
  2: string user_name,
  3: string id_no,
  4: string bank_card_no,
  5: string phone_no,
  6: string access_token,
}

struct SmallPaySignRequest {
  1: string member_no,
  2: string member_order_no,
  3: string trade_order_no,
  4: string result_code,
  5: string sign_value,
}

struct SmallPaySingRepsone {
  1: i32 result_value,
}

service BindThirdpartyService {
  i32 bind_thirdparty(1:BindThirdpartyRequest request),
  RebindChsiResponse send_captcha(1:SendCaptchaRequest request),
  RebindChsiResponse rebind_chsi(1:i64 user_id),
  BindChsiResponse bind_chsi(1:BindChsiRequest request),
  string query_loan(1:QueryLoanRequest request),

  #以下是yunsign的server
  string get_contract_temp_number(1:i32 idx),
  ContractResponse server_create_contract(1:ServerCreateContractRequest request),
  ContractResponse server_create_contract2(1:ServerCreateContract2Request request),
  SendMsgResponse send_msg(1:SendMsgRequest request),
  string show_contract(1:ContactShowRequest request),
  SignResponse sign(1:SignRequest request),
  string download(1:DownloadRequest request),
  GetContractResponse get_contract_status(1:ContractStatusRequest request),
  SmallPayResponse startSmallPay(1: SmallPayRequest request),
  SmallPaySingRepsone checkSmallPaySign(1: SmallPaySignRequest request),
  # 玖富接口对接服务包括 黑名单验证 玖富工单接口等
  i32 check_blacklist(1:CheckBlackListRequest request),

}
