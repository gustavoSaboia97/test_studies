import pytest
import mock

from src.person_service import PersonService


@pytest.mark.describe('Person Service Tests:')
class TestPersonService:

    def setup(self) -> None:
        self.person_service = PersonService()

    @mock.patch('src.person_service.pandas')
    def test_should_read_person_csv(self, mock_pandas: mock.MagicMock) -> None:
        mock_person_df = mock.MagicMock()

        mock_pandas.read_csv.return_value = mock_person_df

        response = self.person_service._read_person_csv()

        mock_pandas.read_csv.assert_called_once_with('./person.csv')

        assert mock_person_df == response
